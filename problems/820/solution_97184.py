def posLetra(frase,letra, n):
    '''retorna o indice da ocrrencia n da letra na frase'''
    parts = frase.split(letra, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(frase) - len(parts[-1]) - len(letra)