'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def main():
    primeFactors(600851475143)

def primeFactors(number):
    factors = []
    result = 1
    appendCounter = 0

    for i in range(2, number):
        if number%i == 0:
            factors.append(i)
            result *= factors[appendCounter]
            appendCounter += 1  

            if result == number:
                break
                
            
    
    print(factors)
    print(f"Largest prime factor is: {factors[-1]}")


if __name__ == "__main__":
    main()
