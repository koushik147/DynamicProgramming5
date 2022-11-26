#TimeComplexity: O(n)
#SpaceComplexity: O(1)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0 # declaring the start value with 0
        end = 0 # declaring the end value with 0
        jumps = 0 # declaring the jumps value with 0
        
        while end<len(nums)-1: # run until the length of nums is greater than end
            farthest = 0 
            for i in range(start,end+1): # run until the loop and set the farthest with the maximum between farthest and nums of ith value
                farthest = max(farthest,i+nums[i])

            jumps+=1 # increment by 1
            start = end+1 # assign end to start
            end = farthest # assign farthest to end
        return jumps # returning the jumps
