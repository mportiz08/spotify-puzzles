#!/usr/bin/env python

"""
catvsdog
~~~~~~~~~~~~~

This is my solution to Spotify's "Cat vs. Dog" Tech Puzzle.
"""

import sys

class Voter(object):
  def __init__(self, vote):
    self.is_dog_person = vote.startswith("D")
    self.is_cat_person = not self.is_dog_person

def parse_test_case(input):
  num_cats, num_dogs, num_voters = [int(i) for i in input.readline().split()]
  
  if num_voters == 0:
    print(num_voters)
    return
  
  votes_keep, votes_throw_out = {}, {}
  voters_parsed = 0
  while(voters_parsed < num_voters):
    vote_keep, vote_throw_out = input.readline().split()
    votes_keep[vote_keep] = votes_keep.get(vote_keep, 0) + 1
    votes_throw_out[vote_throw_out] = votes_throw_out.get(vote_throw_out, 0) + 1
    voters_parsed += 1
  
  sorted_keep = sorted(votes_keep.iteritems())[0][1]
  sorted_throw_out = sorted(votes_throw_out.iteritems())[0][1]
  print(max([sorted_keep, sorted_throw_out]))

def parse_test_cases(input):
  total_test_cases  = int(input.readline().strip())
  test_cases_parsed = 0
  while(test_cases_parsed < total_test_cases):
    parse_test_case(input)
    test_cases_parsed += 1

def main(argv=None):
  parse_test_cases(sys.stdin)
  
  return 0

if __name__ == '__main__':
  status = main()
  sys.exit(status)
