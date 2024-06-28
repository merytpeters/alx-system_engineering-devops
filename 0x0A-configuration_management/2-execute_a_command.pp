# Manifest that kills a process named killmenow

exec { 'killmenow':
  command  => '/usr/bin/pkill -9 killmenow',
  provider => 'shell',
  path     => ['/usr/bin', '/bin'],
  onlyif   => '/usr/bin/pgrep -x killmenow',
}
