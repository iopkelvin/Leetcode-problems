def create_target_array(nums, index):
    '''
     Given two arrays of integers nums and index. Your task is to create target array under the following rules:
        * Initially target array is empty.
        * From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
        * Repeat the previous step until there are no elements to read in nums and index.
    '''
    target = []
    for n, m in zip(index, nums):
        target.insert(n, m)
    print(target)
    return target


if __name__ == '__main__':
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    create_target_array(nums, index)