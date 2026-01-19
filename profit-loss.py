# M1L5 Activity 2
# Topic: Profit and Loss
# This program checks whether there is a profit or a loss

cost_price = 500
selling_price = 650

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit of:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss of:", loss)
else:
    print("No profit, no loss")

# End of program
