# Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.  
# Print the sum of the numbers with comma separators and two digits.

def main():
    sum = 0
    with open('data.txt', 'r') as f:
        for line in f:
            sum += int(line)
    print(sum)
    
if __name__ == '__main__':
    main()