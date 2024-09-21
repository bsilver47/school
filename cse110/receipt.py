#input0
child_price = float(input('How much does the meal of a child cost?  '))
adult_price = float(input('How much does the meal of an adult cost?  '))
child_count = int(input('How many children are there?  '))
adult_count = int(input('How many adults are there?  '))
tax_rate = float(input('What is the local tax rate?  '))

#processing0
subtotal = (child_price * child_count) + (adult_price * adult_count)
total_tax = (subtotal * (tax_rate / 100))
total_price = (subtotal + total_tax)

#output0
print(f'Subtotal: ${subtotal:.02f}')
print(f'Tax: ${total_tax:.02f}')
print(f'Total: ${total_price:.02f}')

#input1 and processing1
paid = float(input("What did they pay?  "))
change = paid - total_price

#output1/ processing2: while loop is to ensure that enough is paid
while change < 0:
    print(f'You still owe: ${change:.02f}')
    total_price = 0 - change
    paid = float(input('What more did they pay?  '))
    change = paid - total_price
    
if change == 0:
    print(f'Thank you for giving exact change. Have a nice day :)')
else:
    print(f'You over paid by:  ${change:.02f}')