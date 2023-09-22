def hashtag(s):
    '''Insere uma # no início, no meio e no final de uma dada string s.'''
    tag = '#'
    nome = str(s)
    return tag + nome[:len(nome)//2] + tag + nome[len(nome)//2:] + tag