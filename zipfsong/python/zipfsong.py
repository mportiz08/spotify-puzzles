#!/usr/bin/env python

"""
zipfsong
~~~~~~~~~~~~~

This is my solution to Spotify's "Zipf's song" Tech Puzzle.
"""

import sys
import heapq

class Song(object):
  def __init__(self, listens, name, track):
    self.listens, self.name, self.track = listens, name, track
  
  def quality(self):
    return self.listens * self.track

def parse_songs():
  first_line     = sys.stdin.readline()
  num_songs      = int(first_line.split()[0])
  num_selections = int(first_line.split()[1])
  
  songs = []
  for i in range(num_songs):
    next_line = sys.stdin.readline()
    
    listens = int(next_line.split()[0])
    name    = next_line.split()[1]
    song    = Song(listens, name, i + 1)
    heapq.heappush(songs, (-song.quality(), song))
  
  return num_selections, songs

def main(argv=None):
  num_selections, songs = parse_songs()
  for i in range(num_selections):
    song = heapq.heappop(songs)[1]
    print(song.name)
  
  return 0

if __name__ == '__main__':
  status = main()
  sys.exit(status)
