def uppCons(frase):
    '''Função que que recebe uma frase e a retorna com todas as suas consoantes em maiúsculas
str -> str'''
    i = 0
    nova_frase = ''

    while i < len(frase):
        letra = frase[i]
        if letra in 'aeiouéãêàôõâ':
            nova_frase = nova_frase + str(letra)
        else:
            nova_frase = nova_frase + str(letra.upper())
        i = i + 1
    return nova_frase