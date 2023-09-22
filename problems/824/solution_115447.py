def uppCons (frase):
    """ Insira uma frase e a função retornara a frase com todas as letras em maiusculo"""
    Q = len(frase)
    I = 0 
    while I < Q:
        if frase[I] in frase:
            letra = frase[I]
            M = str.upper(letra)
            frase = str.replace(frase,letra,M)
        I += 1
    return frase