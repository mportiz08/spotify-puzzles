# An extension to the Fixnum class that provides the following additional methods:
# #msb, #get_bit_val, and #reverse
# 
# This was written as a solution to Spotify's "reversebinary" puzzle.
class Fixnum
  # Finds the "most significant bit" in a value.
  # 
  #   13.msb # => 3
  # 
  # Returns a Fixnum.
  def msb
    orig = self
    pos  = 0
    while orig != 0
      orig = orig >> 1
      pos += 1 if orig != 0
    end
    pos
  end
  
  # Retrieves the value of a specific bit.
  # 
  #   13.get_bit_val(1) # => 0
  #   13.get_bit_val(2) # => 1
  # 
  # bit_pos - an index representing the bit position (from right to left)
  # 
  # Returns a Fixnum (either 1 or 0).
  def get_bit_val(bit_pos)
    (self & ( 1 << bit_pos )) >> bit_pos
  end
  
  # Reverses the value in binary.
  # 
  #   13.reverse # => 11
  #   47.reverse # => 61
  # 
  # Returns a Fixnum.
  def reverse
    orig     = self
    reversed = 0
    
    num_bits = orig.msb + 1
    num_bits.times do |i|
      # check the bit val from the tail end of the original val
      # and set it in the reversed one if necessary
      if orig.get_bit_val(num_bits - 1 - i) == 1
        reversed = reversed | (1 << i)
      end
    end
    
    reversed
  end
end
