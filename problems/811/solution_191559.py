def discriminante(a,b,c):
    return b**2 - 4*a*c
def raizes(a,b,c):
    raiz1 = - b - math.sqrt(discriminante(a,b,c)) / (2*a)
    raiz2 = - b + math.sqrt(discriminante(a,b,c)) / (2*a)
    return (raiz1, raiz2)