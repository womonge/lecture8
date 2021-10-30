#Aprogram to compute profit at 23% of revenue.

def company():

    revenue=float(input("Enter revenue: "))

    profit=(revenue*0.23)

    rounded=round(profit,2) # profit is rounded to 2 decimal place

    print("The profit at 23% of a revenue of Kes.",revenue,"is Kes.",rounded)

company()

    
                
