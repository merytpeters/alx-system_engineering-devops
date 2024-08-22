# Create a new user holberton

user { 'holberton':
  ensure     => 'present',
  managehome => true,
}
