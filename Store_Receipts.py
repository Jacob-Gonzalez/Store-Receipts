# Project Name:  Store-Receipts
# Discription:   Build a program that will gather purchases made by several customers and print out a receipt.
#                Project was provided by Codecademy to test knowledge on basic fundamentals of strings, numbers and updating variables.
# Author:        Jacob Gonzalez (26 July 2023)

# information for sectional couch
sectional_description = """[  2-Piece Sectional with Chaise.  Polyester upholstery with exposed feet.  
Includes right-arm facing chaise, left-arm facing chaise, and four polyfilled throw pillows. 
Additional information:  39 inches high x 123 inches wide x 87 inches deep.  Available in snow, shadow, and navy.\n""" 
sectional_price = 1699.98

# information for ottoman
ottoman_description = """[  Storage ottoman.  Polyester upholstery with storage space under cushioned removable top.  
Additional information:  20 inches high x 37 inches wide x 37 inches deep.  Available in snow, shadow, and navy.\n"""
ottoman_price = 349.99

# information for oversized chair
chair_description = """[  Oversized chair.  Polyester upholstery with three polyfilled back pillows on a 360 degree swivel.  
Additional information:  39 inches high x 58 inches wide x 54 inches deep.  Available in snow, shadow, and navy.\n"""
chair_price = 799.99

# define sales tax
sales_tax = 0.0625

# define customer one totals

customer_one_total = 0
customer_one_itemization = "\n"
customer_one_total += sectional_price
customer_one_itemization += sectional_description + "Price:  $" + str(sectional_price) + "]\n"
customer_one_total += ottoman_price
customer_one_itemization += ottoman_description + "Price:  $" + str(ottoman_price) + "]\n"
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax


# define customer two totals
customer_two_total = 0
customer_two_itemization = "\n"
customer_two_total += sectional_price
customer_two_itemization += sectional_description + "Price:  $" + str(sectional_price) + "]\n"
customer_two_total += ottoman_price
customer_two_itemization += ottoman_description + "Price:  $" + str(ottoman_price) + "]\n"
customer_two_total += chair_price
customer_two_itemization += chair_description + "Price:  $" + str(chair_price) + "]\n"
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

# define customer three totals
customer_three_total = 0
customer_three_itemization = "\n"
customer_three_total = chair_price
customer_three_itemization += chair_description + "Price:  $" + str(chair_price) + "]\n"
customer_three_tax = customer_three_total * sales_tax
customer_three_total += customer_three_tax

# final prints for customer receipt
print("Customer One Items:  ", customer_one_itemization)
print("Final Total (Tax Included):  $%.2f" % customer_one_total, "\n")
print("----------------------------------------------------------------------------------------------------------\n")
print("Customer Two Items:  ", customer_two_itemization)
print("Final Total (Tax Included):  $%.2f" % customer_two_total, "\n")
print("----------------------------------------------------------------------------------------------------------\n")
print("Customer Three Items:  ", customer_three_itemization)
print("Final Total (Tax Included):  $%.2f" % customer_three_total, "\n")

# test prints during development
#print(sectional_description, "\nPrice:  $", sectional_price, "\n")
#print(ottoman_description, "\nPrice:  $", ottoman_price, "\n")
#print(chair_description, "\nPrice:  $", chair_price, "\n")
#print("Current customer total:  $", customer_one_total, "\nCustomer items:  ", customer_one_itemization)
