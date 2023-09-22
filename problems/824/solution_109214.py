def uppCons(frase):
    '''função que recebe uma frase e a retorna com suas consoantes
    em maiúsculas'''
    contador = 0
    troca = ''
    while contador < len(frase):
        troca = frase[contador]
        if frase[contador] not in 'aeiou':
            frase.replace(frase, troca.upper())
        contador = contador + 1
    return frase