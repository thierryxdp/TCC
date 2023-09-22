def uppCons(frase):
    '''Função que dada uma frase retorna todas as suas consoantes em maiusculas, sem alterar as vogais'''
    '''str -> str'''
    tratamento = []
    i = 0
    while i < len(frase):
        consoantes = frase[i]
        if consoantes in 'bcdfghjklmnpqrstvwxzy':
            consoantes = str.upper(consoantes)
        tratamento = tratamento + [consoantes]
        i = i + 1
    return tratamento