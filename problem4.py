#Project Euler Problem 4

def palindrome(n): 
    return str(n) == str(n)[::-1]

def main():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if palindrome(product) and product > largest:
                largest = product
    return largest

largest = main()
print(largest)

 
if __name__ == '__main__':
  main()
