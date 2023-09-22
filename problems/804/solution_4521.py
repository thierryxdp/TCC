def filtra_pares():
    "Função que filtra os números pares de uma tupla com 4 elementos"
    lista1=filtra_pares()
    lista2=[]
    for valor in lista1:
        if valor %2 == 0:
            lista2.append(valor)
            return (lista2)