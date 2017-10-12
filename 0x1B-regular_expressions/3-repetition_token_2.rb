#!/usr/bin/env ruby
puts ARGV[0].scan(/hb[t]+n/).join

# Correct output with: hbtttttn
# Expected hbtttttn
# Got: blank
