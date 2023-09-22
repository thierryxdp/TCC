def soma_h(n):
    s=0
    soma = 1
    cont = 0
    while(cont!=n):
        s += (1/soma)
        soma+=1
        cont+=1
    return round(s,2)