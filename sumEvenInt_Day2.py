nums = list(map(int, input("Enter the list of integers: ").split()))

sum = 0
for n in nums:
    if n%2==0:
        sum += n

print("The Sum of even numbers in the list is:",sum)
