def inverte(frase):
    ''' funcao recebe um frase e retorna ela de tras para frente,sem pontuacao.
    str-->str'''
    pontuacao=',.;:?!'
    for p in pontuacao:
        frase= str.replace(p," ")
        return frase[::--1]