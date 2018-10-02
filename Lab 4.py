print("This program will tell you how much you owe for your monthly phone bill and how much data you used.")

green = "green"
blue = "blue"
purple = "purple"
yes = "yes"
no = "no"
package = input("What subscription package do you have?")
GB = float(input("Please enter how many GB of data you have used this month."))


if package == "green" :
    if GB > 2:
        additional_GB = GB - 2
        monthly_bill = 49.99 + (additional_GB * 15)
    else:
        monthly_bill = 49.99
    coupon = input("Do you have a coupon?")
    if coupon == yes and monthly_bill >= 75:
        monthly_bill = monthly_bill - 20
elif package == "blue" :
    if GB > 4:
        additional_GB = GB - 4
        monthly_bill = 70 + (additional_GB * 10)
    else:
        monthly_bill = 70
elif package == "purple" :
    monthly_bill = 99.95
else:
    print("Invalid entry")
print("You used" , GB , "GB this month!")
print("Your monthly bill is $", monthly_bill)
print("Thank you for using this program!")

