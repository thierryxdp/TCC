def maiores(lista,n):
#Retorna outra lista que contem todos os numeros maiores da lista ordenados
#e em ordem crescente
    a=[]
    for elemento in lista:
        if elemento > n:
            a.append(elemento)
    return a