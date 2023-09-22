def uppCons(frase):
    '''Função que dada uma frase retorna todas as suas consoantes em maiusculas, sem alterar as vogais'''
    '''str -> str'''
    tratamento = []
    i = 0
    while i < len(frase):
        consoantes = frase[i]
        if consoantes in 'bcdfghjklmnpqrstvwxzy':
            consoante = str.upper(consoante)
        i = i + 1
        tratamento = tratamento + consoante
    return tratamento