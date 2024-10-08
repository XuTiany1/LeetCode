class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointers for nums1, nums2 and the merged array
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # While there are elements to compare in nums1 and nums2
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are elements left in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


