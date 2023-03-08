
nums = list(map(int, input().split(" ")))
sum_nums = 0
for i in nums:
    if i >= 0:
        sum_nums = sum_nums + i
    else:
        break
print(sum_nums)
print("end of the loop.....")

