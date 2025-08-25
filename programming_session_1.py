def iterate(items):
    for item in items:
        print(item)

names = ["Ken from Street Fighter", "Neil Armstrong", "Professor", "Water Drinker"]

iterate(names)

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        swap = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
    if not swap: return nums

stuff = [9, 2, 1, -3, 12, 0]
bubble_sort(stuff)
print(stuff)

sorted_nums = [i for i in range(1000)]
bubble_sort(sorted_nums)
print(sorted_nums)