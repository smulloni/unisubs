from django.db.models import ObjectDoesNotExist
from teams.models import TeamVideo

class MultiQuerySet(object):
    def __init__(self, *args, **kwargs):
        self.querysets = args
        self._count = None
    
    def count(self):
        if not self._count:
            """ this can be an expensive calculation. try to set_count first
            if there's a cheaper way to determine the count. """
            self._count = sum(qs.count() for qs in self.querysets)
        return self._count

    def set_count(self, count):
        self._count = count

    def _clone(self):
        mqs = MultiQuerySet(*self.querysets)
        mqs.set_count(self.count())
        return mqs

    def __len__(self):
        """ expensive. try not to call. """
        return self.count()

    def __iter__(self):
        for qs in self.querysets:
            for item in qs.all():
                yield item

    def __getitem__(self, item):
        if isinstance(item, (int, long)):
            offset, stop = item, item + 1
        else: # slice
            offset, stop = item.start, item.stop
        items = []
        total_len = stop - offset
        for qs in self.querysets:
            if len(qs) < offset:
                offset -= len(qs)
            else:
                items += list(qs[offset:stop])
                if len(items) >= total_len:
                    break
                else:
                    offset = 0
                    stop = total_len - len(items)
                    continue
        return items[:total_len]

class MultyQuerySet(object):
    """
    Proxy-object for few QuerySet to be used in Paginator.
    Support only QuerySets for same model.
    """
    
    def __init__(self, *args):
        self.lists = args
        self.model = self.lists[0].model
        
        self._obj_ids = []
        self._cache = {}
        
        for l in self.lists:
            self._obj_ids.extend(l.values_list('pk', flat=True))
        
    def __len__(self):
        return len(self._obj_ids)
    
    def __getitem__(self, k):
        if not isinstance(k, (slice, int, long)):
            raise TypeError
        
        cache_key = k
        if isinstance(k, slice):
            cache_key = '%s:%s:%s' % (k.start, k.stop, k.step)
        
        try:
            return self._cache[cache_key]
        except KeyError:
            pass
        
        val = None
        
        if isinstance(k, (int, long)):
            try:
                val = id._model._default_manager.get(pk=id)
            except ObjectDoesNotExist:
                pass
        else:
            ids = self._obj_ids[k]
            qs = self.get_objects_qs(ids)
            result = dict((obj.pk, obj) for obj in qs)
            val = []
            for id in ids:
                val.append(result[id])
            
        self._cache[cache_key] = val
        return val
        
    def _clone(self):
        return self
    
    def get_objects_qs(self, ids):
        return self.model._default_manager.filter(pk__in=ids)

class TeamMultyQuerySet(object):
    
    def __init__(self, *args):
        self.lists = args
        self._cache = {}
    
    def get_qs_count(self, qs):
        if not hasattr(qs, '_length'):
            qs._length = qs.count()
        return qs._length
    
    def __len__(self):
        if not hasattr(self, '_length'):
            self._length = sum([self.get_qs_count(qs) for qs in self.lists])
        return self._length
    
    def __getitem__(self, k):
        #support only [n] or [n:m], not [:m] or [n:]
        if not isinstance(k, (slice, int, long)):
            raise TypeError
        
        cache_key = k
        if isinstance(k, slice):
            cache_key = '%s:%s:%s' % (k.start, k.stop, k.step)
        
        try:
            return self._cache[cache_key]
        except KeyError:
            pass
        
        val = None
        
        if isinstance(k, (int, long)):
            list_sum = 0
            for qs in self.lists:
                if k < list_sum + self.get_qs_count(qs):
                    cur_index =  list_sum - k
                    val = qs.all()[ k - list_sum ]
                    break
                list_sum += self.get_qs_count(qs)
        else:
            selected = []
            
            k_start = k.start #because readonly
            k_stop = k.stop #because readonly
            
            number = k.stop-k.start
            
            cur_index = 0
            qs_list = []
            for i, qs in enumerate(self.lists):
                if k_start < (cur_index+self.get_qs_count(qs)):
                    qs_list = self.lists[i:]
                    break
                cur_index += self.get_qs_count(qs)
                
            k_start -= cur_index
            k_stop = k_start+number

            for qs in qs_list:
                tl = qs[k_start:k_stop]
                selected.extend(tl)
                k_start = 0
                k_stop = number - len(selected)                    
                if k_stop <= 0:
                    break
            
            val = []
            videos = []
            for obj in selected:
                if hasattr(obj, "team_video") and obj.team_video_id not in videos:
                    videos.append(obj.team_video_id)
                    val.append(obj.team_video)
                elif isinstance(obj, TeamVideo) and obj.id not in videos:
                    videos.append(obj.id)
                    val.append(obj)
            
        self._cache[cache_key] = val
        if val is None:
            raise StopIteration
        return val
        
    def _clone(self):
        return self
    
    def get_objects_qs(self, ids):
        return self.model._default_manager.filter(pk__in=ids)
