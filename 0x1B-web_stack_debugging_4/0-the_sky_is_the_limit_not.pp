# Fixing Apachebenchmark request failure


# Ensure Apache package is installed, put this file in /etc/puppet/modules/apache/manifests/init.pp
class apache {
  package { 'apache2':
    ensure => installed,
  }


  # Ensure Apache service is running and enabled
  service { 'apache2':
    ensure     => running,
    enable     => true,
    hasrestart => true,
    hasstatus  => true,
    require    => Package['apache2'],
  }


  # Ensure the log dir exists
  file { '/var/log/apache2':
    ensure  => directory,
    owner   => 'www-data',
    group   => 'adm',
    mode    => '0755',
    require => Package['apache2'],
  }


  # Ensure the error log file exists with correct permission
  file { '/var/log/apache2/error.log':
    ensure  => file,
    owner   => 'www-data',
    group   => 'adm',
    mode    => '0664',
    require => File['/var/log/apache2'],
  }


  # Ensure the access log file exists with correct permissions
  file { '/var/log/apache2/access.log':
    ensure  => file,
    owner   => 'www-data',
    group   => 'adm',
    mode    => '0664',
    require => File['/var/log/apache2'],
  }
}

# Apply the apache class to the node
include apache

# Execute Apache Benchmark (ab) command, start apache sudo service apache2 start
exec { 'ab':
  command  => '/usr/bin/ab -l -c 100 -n 2000 http://localhost/',
  provider => shell,
  require  => Service['apache2'],
}
