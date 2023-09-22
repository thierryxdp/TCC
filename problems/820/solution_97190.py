def posLetra(frase,letra, n):
    '''retorna o indice da ocrrencia n da letra na frase'''
    qtd=str.count(frase,letra)
    tam=len(frase)
    if qtd<tam:
        return frase.find(letra,n+1)
    else:
        return -1