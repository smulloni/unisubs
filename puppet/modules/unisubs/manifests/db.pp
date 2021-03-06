class unisubs::db {
  class { 'mysql': }
  class { 'mysql::python':
    require => Class['mysql'];
  }
  class { 'mysql::server':
    config_hash => { 'root_password' => 'root' },
    require => Class['mysql'];
  }
  mysql::db { "unisubs":
    require => Class["mysql::server"],
    user => "root",
    password => "root";
  }
}
