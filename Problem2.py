'''
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

#Final version: 0.004000663757324219 seconds
import time
start_time = time.time()

def main():
    evenSumFibonacci()

def evenSumFibonacci():
    sequence = [1,2]
    total = 2
    i = 2

    while True:
        sequence.append(sequence[i-1] + sequence[i-2]) 
        if sequence[i] > 4000000:
          break
        if sequence[i]%2 == 0:
          total += sequence[i]
        i += 1

    print(sequence)
    print(total)
            
if __name__ == "__main__":
    main()
    print(f"--- {time.time() - start_time} seconds ---")
