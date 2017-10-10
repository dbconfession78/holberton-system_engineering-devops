#!/usr/bin/env ruby
 string = ARGV[0]
from = /from:([\+a-z\d]+)/i.match(string)[1]
to = /to:([\+\d]+)/i.match(string)[1]
flags = /flags:([-\d:]+)/i.match(string)[1]
print(from + "," + to + "," + flags)
