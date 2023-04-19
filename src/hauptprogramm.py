from decorators import berechne_dreimal

@berechne_dreimal
def quadrat(x):
    #return x**2
    print (x**2)
    return x**2


print(quadrat(5))
