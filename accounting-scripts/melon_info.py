"""Print out all the melons in our inventory."""


from melons import melons
# melon_names, melon_seedlessness, melon_prices

def print_all_melons(melons):
    """Print each melon with corresponding attribute information"""

    for melon_name, attributes in melons.items(): #pulls out the first key, and 
    #the dictionary associated to it and naming that attributes
        print(melon_name.upper()) #print melon name in caps

        for attribute, value in attributes.items(): #loop through the attribute
        #dictionary and pulls attribute keys and the values for them
            print(f'{attribute}: {value}')

        print('==================================')

print_all_melons(melons)


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
