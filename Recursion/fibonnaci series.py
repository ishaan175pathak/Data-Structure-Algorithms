# creating a fibonnaci series using recursion

def fibonnaci_series(n):

    if n <= 1:
        return (n,0)
    else:
        a,b = fibonnaci_series(n-1)
        print(a+b,end=" ")
        return (a+b,a)


fibonnaci_series(int(input("Enter the Range: "))