# Main Page: https://leetcode.com/list/52657ph7/


# https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()
    print(nums3)

    if len(nums3) == 0:
        return "this is an empty list"

    if len(nums3) == 1:
        return nums3[0]

    if len(nums3) % 2 == 0:
        m1 = int(len(nums3) / 2)
        m2 = int(m1 - 1)
        return (nums3[m1] + nums3[m2]) / 2

    else:
        middle = ((len(nums3) - 1) / 2)
        return nums3[int(middle)]





print(findMedianSortedArrays([1,2,6,9,10], [3,4,5,6,7]))




