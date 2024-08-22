# Create a new user holberton

user { 'holberton':
  ensure     => 'present',
  managehome => true,
  shell      => '/bin/bash',
  home       => '/home/holberton',
  groups     => ['sudo', 'www-data'],
}

# Ensure the soft limit for open files is set for the holberton user
exec { 'set_soft_nofile_limit':
  command => 'echo "holberton soft nofile 65536" >> /etc/security/limits.conf',
  unless  => 'grep -q "^holberton soft nofile" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}

# Ensure the hard limit for open files is set for the holberton user
exec { 'set_hard_nofile_limit':
  command => 'echo "holberton hard nofile 65536" >> /etc/security/limits.conf',
  unless  => 'grep -q "^holberton hard nofile" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}
