import collections
from  Contains_Duplicate_III import Solution
So=Solution()
nums=[1,7];
istrue=Solution.containsNearbyAlmostDuplicate(Solution,nums,2,30)
print (istrue)

k=2
t=30

dic = collections.OrderedDict()
        
for i in range(len(nums)):
    key = nums[i] / max(1, t)
        
    for m in (key, key - 1, key + 1):
        if m in dic and abs(nums[i] - dic[m]) <= t:
            istrue=True
                
        dic[key] = nums[i]
            
        if i >= k:
            dic.popitem(last=False)
    istrue=False
