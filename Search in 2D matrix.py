#Time Complexity:: Average: O(logn)-Traversing with for loop using Binary Search
#Space Complexity:: Almost O(1) - no extra space since we're just finding index
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix) #every array inside the matrix array is a row, so this is no. of rows
        n=len(matrix[0]) #every array inside array has the same length, which is the no. of columns 
        
        l=0 #starts at index 0
        h=m*n-1 #starts at last index
        
        while l<=h: #ensures l and h are correct and '=' makes sure to check mid when l&h meet
            mid=l+(h-l)//2 #also prevents integer overflow
            num = matrix[mid//n][mid%n] #finding the element in the mid index
            if num==target: #checking mid index value
                return True
            elif target<num: #checking to traverse left of the mid
                h=mid-1 #change high to search left of mid
            else: #traverse right of the mid
                l=mid+1 #change low to search right of mid
        return False #returns false if not present
