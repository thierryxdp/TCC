def filtra_pares(n1,n2,n3,n4):
    lista1 = [n1,n2,n3,n4]
    lista2 = []
    for valor in lista1:
        if valor % 2 ==0:
            lista2.append(valor)
            
print(lista2)