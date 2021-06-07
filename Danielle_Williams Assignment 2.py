# Author: Danielle R. Williams
# Date: June 6, 2021
# Input: User enters the amount of change due to the customer
# Processing: The program calculates the coins that are due by using division properties and identifying int
# Output: After doing the calculations, program displays the change in the amount of each denomination of coins

def main():
    n=int(input("How much change is due?:"))
    print(n//25, "quarters")
    n = n%25
    print(n//10, "dimes")
    n = n%10
    print(n//5, "nickles")
    n = n%5
    print(n//1, "pennies")

main() 
