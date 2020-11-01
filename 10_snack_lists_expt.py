# Initialise snack lists...

popcorn = []
mms = []
pita_chips = []
water = []

snack_lists = [popcorn, mms, pita_chips, water]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms
    }

# Assume no snacks have been bought...
for item in snack_lists:
    item.append(0)

# get order (hard coded for easy testing)...
snack_order = [[1, 'Water'], [1, 'Pita Chips'], [1, 'M&Ms']]

for item in snack_order:
    to_find = (item[1])
    amount = (item[0])
    add_list = snack_menu_dict[to_find]
    add_list[-1] = amount

print(snack_lists)


