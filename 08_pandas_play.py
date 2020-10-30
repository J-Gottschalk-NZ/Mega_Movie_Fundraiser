import pandas

# dictionary to hold snack prices
snack_prices = {
    "Popcorn": 2.5,
    "M&Ms": 3,
    "Pita Chips": 4.5,
    "Orange Juice": 3.25,
    "Water": 2
}


# data-frame to hold snack numbers,
# initially set amounts to zero
data = {'Snack':  ['Popcorn', 'M&Ms','Pita Chips', 'Orange Juice', 'Water'],
        'Amount': [0, 0, 0, 0, 0]
        }

df = pandas.DataFrame(data, columns=['Snack', 'Amount'])

print(df)

print()

# identify row using index and change it
df.at[4, 'Amount'] = 5

print(df)

print()

print("*** add to popcorn count ***")
popcorn_count = df.at[0, 'Amount']
popcorn_count += 3
df.at[0, 'Amount'] = popcorn_count

print(df)
