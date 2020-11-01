import pandas

# imports dataframe from csv file
# trial pandas.read_excel(*args, **kwargs) to
# read in an xlsx file rather than a .csv
df = pandas.read_csv("Assets/04_MM_ticket_price_list.csv")

df = df.set_index('Item')

print(df)
print()

# Test Data

snack_orders = [
    [1, "Pita Chips"],
    [3, "Popcorn"],
    [2, "Water"],
    [1, "Orange Juice"]
]

ticket_price = 6.5

# Put snack orders into data frame
for item in snack_orders:
    df.at[item[1], 'Num Sold'] = item[0]

# put in ticket_price
df.at['Ticket', 'Cost'] = ticket_price
df.at['Ticket', 'Num Sold'] = 1

# create column called price
# fill it with number sold x cost
df["Price"] = df["Num Sold"] * df["Cost"]

# Find total price of snacks
total_snack_cost = df['Price'].sum()

print("***** After Orders *****")
print(df)

print()
# Print non-zero rows only
non_zero = df.loc[df["Price"] != 0]

print(non_zero)
print()

print("Total Snack Cost: ${:.2f}".format(total_snack_cost))
