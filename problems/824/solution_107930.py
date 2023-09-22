def uppCons(frase):
    '''Dada uma frase, a função retorna a mesma mas com suas consoantes
       como maiúsculas(caso já não fossem)
       str -> str
       Parametros:
       frase: frase a ser escolhida e digitada'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUãõáóíéúÃÕÁÉÍÓÚ':
            frase = frase.replace(frase[i], str.upper(frase[i]))
        i += 1
    return frase