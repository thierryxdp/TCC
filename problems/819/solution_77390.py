def filtraMultiplos(lista:int,n:int)->list:
    """ A funcao recebe uma lista de numeros, e um numero n.Ela calcula quais numeros da lista sao multiplos desse numero n, utilizando o modulo de cada numero dessa lista com esse numero n, que dê zero. Ela retorna uma nova lista com os elementos da lista original que forem divisíeis pelo numero n"""
    indice = 0
    resposta = list()
    while (indice < len(lista)):
        if (lista[indice] % n == 0):
            resposta += [lista[indice],]
        indice += 1
        
        return resposta