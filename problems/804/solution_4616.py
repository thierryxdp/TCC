def par (a,b,c,d):
    return  (a%2,b%2,c%2,d%2) !=1
tupla = tuple(filter(par(a,b,c,d),(a,b,c,d)))
print(tupla)