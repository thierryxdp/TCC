def hashtag(s):
    '''Função que retorna uma string e insere '#' no início, no meio e no final dela.
    str->str'''
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:]+'#'