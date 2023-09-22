def uppCons(frase):
    '''Função que recebe uma frase como entrada e retorna essa
    frase com todas as consoantes em maiúsculas
    str -> str'''
    contador = 0
    str_consoante = 'qwrtypsdfghjklçzxcvbnm'
    while contador < len(frase):
        if frase[contador] in str_consoante:
            frase = frase[:contador] + str.upper(frase[contador]) + frase[contador + 1:]
        contador += 1
    return frase