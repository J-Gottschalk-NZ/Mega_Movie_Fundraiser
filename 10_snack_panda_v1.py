import pandas

names = ["John", "Henry", "James"]
ticket = [6.5, 10.5, 7.50]
popcorn = [0, 1, 0]
mms = [0, 0, 0]
pita_chips = [1, 0, 1]
water = [3, 2, 1]

snack_dict = {
    'name': names,
    'ticket': ticket,
    'popcorn': popcorn,
    'mms': mms,
    'pita': pita_chips,
    'water': water
}

snack_frame = pandas.DataFrame(snack_dict)

print(snack_frame)


