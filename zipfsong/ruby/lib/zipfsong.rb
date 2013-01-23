module Zipfsong
  def self.select_songs(num_songs, num_selections, songs)
    SongSelector.new(num_songs, num_selections, songs).select
  end
  
  class Song
    attr_reader :listens, :name, :track
    
    def initialize(listens, name, track)
      @listens, @name, @track = listens, name, track
    end
    
    def <=>(other)
      if (other.quality <=> quality).zero?
        track <=> other.track
      else
        other.quality <=> quality
      end
    end
    
    def quality
      listens * track
    end
  end
  
  class SongSelector
    def initialize(num_songs, num_selections, songs)
      @num_songs, @num_selections, @songs = num_songs, num_selections, songs
    end
    
    def select
      @songs.sort[0...@num_selections]
    end
  end
end
