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
  command => '/bin/sed -i "/^holberton.*soft.*nofile/c\holberton soft nofile 50000" /etc/security/limits.conf',
  unless  => '/bin/grep -q "^holberton soft nofile 50000" /etc/security/limits.conf',
  path    => ['/usr/local/bin', 'bin', '/usr/bin'],
}

# Ensure the hard limit for open files is set for the holberton user
exec { 'set_hard_nofile_limit':
  command => '/bin/sed -i "/^holberton.*hard.*nofile/c\holberton hard nofile 50000" /etc/security/limits.conf',
  unless  => '/bin/grep -q "^holberton hard nofile 50000" /etc/security/limits.conf',
  path    => ['/usr/local/bin', 'bin', '/usr/bin'],
}
