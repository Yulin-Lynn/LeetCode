class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
            
        from collections import Counter
        c1 = Counter(nums1)
        ans = []
        for n in nums2:
            if n in nums2 and c1[n] > 0:
                ans.append(n)
                c1[n] -= 1
        return ans
