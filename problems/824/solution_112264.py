def uppCons(frase):
    '''Função que recebe uma frase qualquer e retorna a mesma frase com todas as consoantes maiúsculas.
str --> str'''
    i = 0
    frase_final = ''
    while i < len(frase):
        if frase[i] in 'ÃãÀàÁáAEÉéÍíIÓóÔôOUúÚaeiou':
            frase_final = frase_final + frase[i]
        else:
            frase_final = frase_final + frase[i].upper()
        i = i+1
    return frase_final