# leetcode #26 删除重复项

def removeDuplicates(self, nums: list[int]) -> int:
    if not nums:
        return 0
    stack = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != stack[-1]:
            stack.append(nums[i])
    for i in range(len(stack)):
        nums[i] = stack[i]
    return len(stack)