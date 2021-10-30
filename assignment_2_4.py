# A program that computes a given integer power.
# y= x*x*x....*n


def main():

    x=int(input("enter the value of x :"))

    n=int(input("enter the value of n :"))

    power=1

    for i in range(1,n+1):

        power=power*x
        
    print(power)

main()




