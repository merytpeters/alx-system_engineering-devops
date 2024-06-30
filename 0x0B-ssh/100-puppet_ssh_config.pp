# Make changes, set up client SSH config file

file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "\
Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
",
}
