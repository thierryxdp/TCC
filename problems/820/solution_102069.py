def posLetra(frase, letra, ocorrencia):
    '''retorna em que posição da string aquela ocorrência da letra está; str, str, int -> int'''

    contador = 0
    lista = list(frase)

    if str.count(frase,letra)<ocorrencia:
        return -1
    else:
        for i in range(0,len(lista)):
            if lista[i] == letra:
                contador = contador + 1
            if contador == ocorrencia:
                return i