#Task4 : Dictionary

#2. dictionary
my_expenses = {"Hotel": 1500, "Food": 800, "Transportation": 500, "Attractions": 300, "Movie": 200,"Shopping":300}
partner_expenses = {"Hotel": 1200, "Food": 900, "Transportation": 600, "Attractions": 400, "Movie": 450, "Shopping":250}

print("My Expense: ",my_expenses)
print("Partner's Expense: ",partner_expenses)

my_total = sum(my_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nMy Total Expense: ",my_total)
print("Partner's Total Expense: ",partner_total)

if my_total>partner_total:
    print("\nI spent more")
elif partner_total>my_total:
    print("\nPartner spent more")
else:
    print("\nBoth spent equally")
    
diff = 0
diff_category = ""

for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expenses[category])
    if difference > diff:
        diff = difference
        diff_category = category

print(f"The largest spending difference was in '{diff_category}' with a difference of ₹{diff}.")
