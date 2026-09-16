class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        5 => 101
        bitmask = 1 *2 * 2
        101
         10
        
        1 + 0 + 
        """
        bitmask = 1
        count = 0
        for i in range(32):
            if n & bitmask != 0:
                count += 1
            bitmask = bitmask << 1
        return count