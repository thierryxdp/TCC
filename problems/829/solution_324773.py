def soma_h(num):
    lista=list(range(2,num+1))
    H=1
    for n in lista:
        H=(1/n)+ H
    return round(H,2)