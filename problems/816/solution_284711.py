def maiores(lista,n):
    "Função que tenha numeros inteiros e roterne uma lista com os numero maiores que o numero maiores que n"
    listi=[]
    for x in lista:
        if x>n:
            listi.append(x)
            list.sort(listi)
    return listi