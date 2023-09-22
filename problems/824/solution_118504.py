def uppCons(frase):
    '''
    função que recebe uma frase e retorna a mesma frase com suas consoantes em
    maiúsculo
    str->str
    '''
    lista_consoantes = []
    proximo = 0 
    while proximo < len(frase):
        if frase[proximo] not in 'aeiou':
            lista_consoantes = lista_consoantes + [str.upper(frase[proximo])]
        else:
            lista_consoantes = lista_consoantes + [frase[proximo]]
        proximo = proximo + 1
    return str.join('', lista_consoantes)