def min_notes(amount, denominations):
    breakdown = {}
    for denom in denominations:
        count = amount // denom
        if count > 0:
            breakdown[denom] = count
        amount %= denom
    return breakdown

def current_results(label, breakdown, denominations):
    print("Currency Notes                ->", end=" ")
    for denom in denominations:
        print(f"{denom:10}", end=" ")
    print(f"{label}->", end=" ")
    for denom in denominations:
        print(f"{breakdown.get(denom, 0):10}", end=" ")
    print()

def total_results(label, breakdown, denominations):
    print(f"{label}->", end=" ")
    for denom in denominations:
        print(f"{breakdown.get(denom, 0):10}", end=" ")
    print()
    
def main():
   
    denominations = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
    total_breakdown = {denom: 0 for denom in denominations}

    while True:
        try:
            print("\nEnter the amount  -  ", end="")
            amount = int(input())
            if amount <= 0:
                print("Amount must be a positive integer. Please enter again.")
                continue

            current_breakdown = min_notes(amount, denominations)

            for denom, count in current_breakdown.items():
                total_breakdown[denom] += count

            
            current_results(f"\nCurrent Breakdown [{amount}]     ", current_breakdown, denominations)

            
            total_results("Total Breakdown              ", total_breakdown, denominations)

            
            option=input("Do you want to continue ? [Yes] or [No] ) :").strip().lower()
            if option !="yes": 
                print("\nBye for now!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()
