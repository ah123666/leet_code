print('hello world')
def getTargetSum(nums, targrt):
    length = len(nums)
    location = []
    for i in range(0, length - 1):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                location.append(i)
                location.append(j)
    return location

nums = [2, 7, 2, 15]
target = 9
location = getTargetSum(nums, target)
print(location)

         
          