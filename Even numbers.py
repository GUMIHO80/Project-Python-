
def even_numbers(n):
    even_nums = ['0', '2', '4', '6', '8']
    counter = 0
    n = str(n)
    
    for char in n:
         if char in even_nums:
            counter += 1
    return counter


n = int(input("enter a number:"))

print(even_numbers(n))
