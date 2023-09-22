def lingua_p(palavra):
    i = 0
    lista = []
    resposta = []
    while (i<len(palavra)):
        lista = [palavra[i],]
        i += 1
        for letra in lista:
            if (letra in 'aeiou'):
                lista=lista.insert(lista[letra],letra+'p'+letra)
                resposta = lista.extend(lista)
        return resposta[-1]