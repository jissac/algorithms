#

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    if nums1 > nums2:
        nums1,nums2 = nums2,nums1
    hash1 = {}
    out = []
    for num in nums1:
        if num in hash1:
            hash1[num] +=1
        else:
            hash1[num] = 1

    for num in nums2:
        if num in hash1 and hash1[num]>0:
            out.append(num)
            hash1[num] -= 1
    return out

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [1,1]

    result = intersect(nums1,nums2)
    print(result)