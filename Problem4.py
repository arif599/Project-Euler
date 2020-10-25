'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def main():
    palindromicNum(100,1000)

def palindromicNum(rangeStart, rangeEnd):
    largePalindromic = 0

    for i in range(rangeStart, rangeEnd):
        for j in range(i-rangeStart, rangeEnd):
            if i*j == reverse(str(i*j)):
                largePalindromic = i*j
    print(largePalindromic)

def reverse(string): 
  reverse_str = "" 

  for i in string: 
    reverse_str = i + reverse_str
  return int(reverse_str)

if __name__ == "__main__":
    main()