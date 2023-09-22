def posLetra(frase,letra, n):
    '''retorna o indice da ocrrencia n da letra na frase'''
    qtd=str.count(frase,letra)
    frasi=list(frase)
    tam=len(frasi)
    if qtd<tam:
        return frase.find(letra,n)
    else:
        return -1