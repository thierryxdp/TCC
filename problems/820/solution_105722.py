def posLetra (frase, letra, indice):
    lista = list(frase)
    i = 0
   	posicao = []
    while i <= len(lista):
        if lista[i] == letra:
       		return posicao.append(i)
        i =+ 1