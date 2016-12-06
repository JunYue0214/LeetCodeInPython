import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
            
        dic = collections.OrderedDict()
        
        for i in range(len(nums)):
            key = nums[i] / max(1, t)
            
            for m in (key, key - 1, key + 1):
                if m in dic and abs(nums[i] - dic[m]) <= t:
                    return True
                
            dic[key] = nums[i]
            
            if i >= k:
                dic.popitem(last=False)
        return False
