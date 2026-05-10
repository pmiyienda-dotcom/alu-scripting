#!/usr/bin/env ruby

# Extract sender, receiver and flags using regex
sender = ARGV[0].scan(/\[from:(.*?)\]/).flatten.first || ""
receiver = ARGV[0].scan(/\[to:(.*?)\]/).flatten.first || ""
flags = ARGV[0].scan(/\[flags:(.*?)\]/).flatten.first || ""

puts "#{sender},#{receiver},#{flags}"