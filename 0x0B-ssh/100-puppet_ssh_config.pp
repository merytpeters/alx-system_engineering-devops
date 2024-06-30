# Make changes, set up client SSH config file

file { '/root/.ssh/config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "\
Host 3.84.238.65
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
",
}
