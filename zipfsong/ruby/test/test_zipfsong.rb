require 'test/unit'
require 'zipfsong'

class TestZipfsong < Test::Unit::TestCase
  def test_sample_one
    songs = [
      Zipfsong::Song.new(30, 'one', 1),
      Zipfsong::Song.new(30, 'two', 2),
      Zipfsong::Song.new(15, 'three', 3),
      Zipfsong::Song.new(25, 'four', 4)
    ]
    assert_equal ['four', 'two'], Zipfsong.select_songs(4, 2, songs).map(&:name)
  end
  
  def test_sample_two
    songs = [
      Zipfsong::Song.new(197812, 're_hash', 1),
      Zipfsong::Song.new(78906, '5_4', 2),
      Zipfsong::Song.new(189518, 'tomorrow_comes_today', 3),
      Zipfsong::Song.new(39453, 'new_genious', 4),
      Zipfsong::Song.new(210492, 'clint_eastwood', 5),
      Zipfsong::Song.new(26302, 'man_research', 6),
      Zipfsong::Song.new(22544, 'punk', 7),
      Zipfsong::Song.new(19727, 'sound_check', 8),
      Zipfsong::Song.new(17535, 'double_bass', 9),
      Zipfsong::Song.new(18782, 'rock_the_house', 10),
      Zipfsong::Song.new(198189, '19_2000', 11),
      Zipfsong::Song.new(13151, 'latin_simone', 12),
      Zipfsong::Song.new(12139, 'starshine', 13),
      Zipfsong::Song.new(11272, 'slow_country', 14),
      Zipfsong::Song.new(10521, 'm1_a1', 15)
    ]
    assert_equal ['19_2000', 'clint_eastwood', 'tomorrow_comes_today'],
                 Zipfsong.select_songs(15, 3, songs).map(&:name)
  end
end
