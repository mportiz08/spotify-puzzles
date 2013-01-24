#!/usr/bin/env python

"""
catvsdog
~~~~~~~~~~~~~

This is my solution to Spotify's "Cat vs. Dog" Tech Puzzle.
"""

import sys
import operator

class Voter(object):
  def __init__(self, vote):
    self.is_dog_person = vote.startswith("D")
    self.is_cat_person = not self.is_dog_person

def highest_dict_val(dict):
  sdict = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=True)
  return sdict[0][1]

def parse_test_case(input):
  num_cats, num_dogs, num_voters = [int(i) for i in input.readline().split()]
  
  if num_voters == 0:
    print(num_voters)
    return
  
  # initialize votes for all cats/dogs
  votes_keep, votes_throw_out = {}, {}
  for i in range(num_cats):
    key = "C" + str(i + 1)
    votes_keep[key] = 0
    votes_throw_out[key] = 0
  for i in range(num_dogs):
    key = "D" + str(i + 1)
    votes_keep[key] = 0
    votes_throw_out[key] = 0
  
  # keep track of votes for/against pets
  voters_parsed = 0
  while(voters_parsed < num_voters):
    vote_keep, vote_throw_out = input.readline().split()
    votes_keep[vote_keep] = votes_keep[vote_keep] + 1
    votes_throw_out[vote_throw_out] = votes_throw_out[vote_throw_out] + 1
    voters_parsed += 1
  
  # a cat with no votes for/against satisfies everyone
  for i in range(num_cats):
    key = "C" + str(i + 1)
    if votes_keep[key] == 0 and votes_throw_out[key] == 0:
      votes_keep[key] = num_voters
      votes_throw_out[key] = num_voters
  
  # a dog with no votes for/against satisfies everyone
  for i in range(num_dogs):
    key = "D" + str(i + 1)
    if votes_keep[key] == 0 and votes_throw_out[key] == 0:
      votes_keep[key] = num_voters
      votes_throw_out[key] = num_voters
  
  most_kept       = highest_dict_val(votes_keep)
  most_thrown_out = highest_dict_val(votes_throw_out)
  
  max_people_satisfied = max([most_kept, most_thrown_out])
  print(max_people_satisfied)

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
