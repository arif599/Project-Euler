'''
Multiples of 3 and 5
Problem 1 (https://projecteuler.net/problem=1)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

ANSWER: 233168
'''

def main():
    print(sumOfMultiples(3,5,10))
    print(sumOfMultiples(3,5,1000))

def sumOfMultiples(mult1, mult2, rangeOfNum):
    listOfMultiples = []
    total = 0

    for i in range(1, rangeOfNum):
        if i%mult1 == 0 or i%mult2 == 0:
            listOfMultiples.append(i)
    
    total = sum(listOfMultiples)
    return total

if __name__ == "__main__":
    main()

