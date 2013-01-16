#!/usr/bin/env python

import sys

def most_significant_bit(num):
  pos = 0
  while num != 0:
    num = num >> 1
    if num != 0:
      pos += 1
  
  return pos

def get_bit_val(num, bit_pos):
  return (num & ( 1 << bit_pos )) >> bit_pos

def reverse_binary_number(num):
  reversed = 0
  num_bits = most_significant_bit(num) + 1
  
  for i in range(num_bits):
    if get_bit_val(num, num_bits - 1 - i) == 1:
      reversed = reversed | (1 << i)
  
  return reversed

def main():
  orig_num = int(sys.stdin.readline())
  reversed = reverse_binary_number(orig_num)
  
  print(str(reversed))

if __name__ == '__main__':
  main()
