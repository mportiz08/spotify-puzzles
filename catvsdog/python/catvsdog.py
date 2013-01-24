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
  
  voters = []
  num_dog_lovers, num_cat_lovers = 0, 0
  while(len(voters) < num_voters):
    voter = Voter(input.readline().strip())
    voters.append(voter)
    if voter.is_dog_person: num_dog_lovers += 1
    if voter.is_cat_person: num_cat_lovers += 1
  
  num_satisfied = 0
  if num_dog_lovers == num_cat_lovers:
    num_satisfied = num_dog_lovers
  else:
    num_satisfied = max([num_dog_lovers, num_cat_lovers])
  
  print str(num_satisfied)

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
