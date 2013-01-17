#!/usr/bin/env python

"""
zipfsong
~~~~~~~~~~~~~

This is my solution to Spotify's "Zipf's song" Tech Puzzle.
"""

import sys
from functools import cmp_to_key

class Song(object):
  def __init__(self, listens, name, track):
    self.listens, self.name, self.track = listens, name, track
  
  def quality(self):
    return self.listens * self.track

class SongSelector(object):
  def __init__(self, num_songs, num_selections, songs):
    self._num_songs, self._num_selections = num_songs, num_selections
    self._songs = songs
  
  def select(self):
    sorted_songs = sorted(self._songs, key=cmp_to_key(compare_songs))
    
    return sorted_songs[:self._num_selections]

def compare_songs(a, b):
  if a.quality() < b.quality():
    return 1
  elif a.quality() > b.quality():
    return -1
  else:
    if a.track < b.track:
      return -1
    elif a.track > b.track:
      return 1
    else:
      return 0

def parse_songs():
  first_line = sys.stdin.readline()
  rest_lines = sys.stdin.readlines()
  
  num_songs      = int(first_line.split()[0])
  num_selections = int(first_line.split()[1])
  
  songs = []
  for i, line in enumerate(rest_lines):
    listens = int(line.split()[0])
    name    = line.split()[1]
    songs.append(Song(listens, name, i + 1))
  
  return num_songs, num_selections, songs

def main(argv=None):
  num_songs, num_selections, songs = parse_songs()
  selection = SongSelector(num_songs, num_selections, songs).select()
  for song in selection:
    print song.name
  
  return 0

if __name__ == '__main__':
  status = main()
  sys.exit(status)
