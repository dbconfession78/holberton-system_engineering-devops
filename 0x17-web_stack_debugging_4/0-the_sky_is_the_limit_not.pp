# fixes bug where nginx max open files is set to 15. Fix raises it to 4096
exec {'change limit from 15 to 15000 in /etc/default/nginx':
  command => '/bin/sed -i "s@ULIMIT=\"-n 15\"@ULIMIT=\"-n 15000\"@" /etc/default/nginx && /etc/init.d/nginx restart',
}
