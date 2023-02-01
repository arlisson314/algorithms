from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):

    merge_sort(nums)

    for i in range(len(nums) - 1):

        if not nums or not isinstance(nums[i], int):
            return False
        if nums[i] < 0:
            return False

        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
