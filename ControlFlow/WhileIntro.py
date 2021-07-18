# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

print("*" * 80)

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)

print("*" * 80)

start_num = 5
end_num = 100
count_by = 5

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

print(break_num)