def melon_totals_by_type(orders_by_type_file):
    """return the total sales by melon type including price"""

    melon_sales = open(orders_by_type_file)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    for sales in melon_sales:
        sales = sales.rstrip()
        sales = sales.split('|')
        melon_type = sales[1]
        melon_count = int(sales[2])
        melon_tallies[melon_type] += melon_count

    melon_sales.close()

    return melon_tallies


def total_revenue(melon_tallies):  
    melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00}
    total_revenue = 0

    print("Total Revenue")

    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print(f"We sold {melon_tallies[melon_type]:,} {melon_type} melons at ${price:,.2f} each for a total of ${total_revenue:,.2f}")



def sales_comparison(orders_with_sales_file):
    orders = open(orders_with_sales_file)
    online_revenue = 0
    salespeople_revenue = 0

    for order in orders:
        order = order.rstrip()
        order = order.split('|')
        sales_type = order[2]
        sales_total = order[3]

        if sales_type == "ONLINE":
            online_revenue += float(sales_total)

        else:
            salespeople_revenue += float(sales_total)

    print("SALES DATA")
    print(f"Salespeople generated ${salespeople_revenue:,.2f} in revenue.")
    print(f"Internet sales generated ${online_revenue:,.2f} in revenue.")

    if online_revenue > salespeople_revenue:
        print("Time to fire the sales team! Online sales rule all!")

    else:
        print("Guess there's some value to those salespeople after all.")

    orders.close()

melon_tallies = melon_totals_by_type("orders-by-type.txt")
total_revenue(melon_tallies)
print()
sales_comparison("orders-with-sales.txt")
# SALESPERSON_INDEX = 0
# INTERNET_INDEX = 1
# DORKY_LINE_LENGTH = 80

# print("*" * DORKY_LINE_LENGTH)
# f = open("orders-by-type.txt")
# melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

# for l in f:
#     data = l.split("|")
#     melon_type = data[1]
#     melon_count = int(data[2])
#     melon_tallies[melon_type] += melon_count

# f.close()
# melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
# total_revenue = 0
# for melon_type in melon_tallies:
#     price = melon_prices[melon_type]
#     revenue = price * melon_tallies[melon_type]
#     total_revenue += revenue
#     # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
#     print("We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue))
# print("******************************************")
# f = open("orders-with-sales.txt")
# sales = [0, 0]
# for line in f:
#     d = line.split("|")
#     if d[1] == "0":
#         sales[0] += float(d[3])
#     else:
#         sales[1] += float(d[3])
# print("Salespeople generated ${:.2f} in revenue.".format(sales[1]))
# print("Internet sales generated ${:.2f} in revenue.".format(sales[0]))
# if sales[1] > sales[0]:
#     print("Guess there's some value to those salespeople after all.")
# else:
#     print("Time to fire the sales team! Online sales rule all!")
# print("******************************************")
