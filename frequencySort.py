def frequencySort(nums):
    record_dict = {}
    for i in nums:
        if i not in record_dict:
            record_dict[i] = 1
        else:
            record_dict[i] += 1
    print('dict ', record_dict)
    print('nums ', nums)
    print('sort ', sorted(nums, key=lambda x: (record_dict[x], -x)))

    return


if __name__ == "__main__":
    nums = [1,1,1,2,2,2,3]
    print(frequencySort(nums))