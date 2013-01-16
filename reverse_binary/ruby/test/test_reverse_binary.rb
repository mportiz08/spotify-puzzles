require 'test/unit'
require 'reverse_binary'

class TestReverseBinary < Test::Unit::TestCase
  def test_spotify_samples
    assert_equal 11, 13.reverse
    assert_equal 61, 47.reverse
  end
end
