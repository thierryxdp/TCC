def uppCons(frase):
    '''função que recebe uma frase e a retorna com suas consoantes
    em maiúsculas'''
    contador = 0
    troca = ''
    while contador < len(frase):
        if frase[contador] is not upper and is not in 'aeiou':
            troca = frase[contador]
            frase.replace(frase[contador], troca.upper())
    return frase