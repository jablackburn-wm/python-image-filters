from filter import filter
from keys import *

keys_table = {
    "all_keys": all_keys,
    "basic_keys": basic_keys,
    "swap_keys": swap_keys,
    "invert_keys": invert_keys,
    "swap_invert_keys": swap_invert_keys,
    "rx_swap_keys": rx_swap_keys,
    "rx_invert_keys": rx_invert_keys,
    "gx_swap_keys": gx_swap_keys,
    "gx_invert_keys": gx_invert_keys,
    "bx_swap_keys": bx_swap_keys,
    "bx_invert_keys": bx_invert_keys,
}

# origin = input("origin:")
# folder = input("folder:")
# name = input("endpoint:")
# rmult = int(input("rmult:"))
# gmult = int(input("gmult:"))
# bmult = int(input("bmult:"))

origin = 'blue-shaded-wfigure102-black-white-purplized.png'
folder = 'blue-shaded-wfigure102-black-white-purplized'
name = 'blue-shaded-wfigure102-black-white-purplized'
mult = [1, 1, 1]
add = [0, 0, 0]
keys = 'all_keys'

print("eating pixels...")
print("eating pixels...")
print("eating pixels...")

filter(origin, folder, name, mult, add, keys_table[keys])
