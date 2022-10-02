class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = low +(high-low)//2
            
            if nums[mid]==target: #only condition that outputs index of the element being searched
                return mid
            elif nums[low]<=nums[mid]: #left-checking if left side is sorted
                if nums[low]<=target and target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else: #right-checking if right side is sorted
                if nums[mid]<target and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1 #if the element being searched isn't in the arry then return -1
