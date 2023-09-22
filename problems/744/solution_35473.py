def hashtag(s):
    '''Função que insere o caractere # no início, no meio
    e no final da palavra.
    str->str'''
    meio=len(s)//2
    resto=s[len(s)//2:]
    return '#'+s[:meio]+'#'+resto+'#'