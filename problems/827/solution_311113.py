def qtd_divisores(numero):
    "Informa a quantidade de divisores de um número"
    contador = 0
    lista = list(range(numero)),numero)
    list.append(lista,numero)
    
    for divisores in lista:
        if divisores > 0:
            if numero%divisores == 0:
                contador += 1
    return contador