def hashtag(s):
    '''Função que dada uma string s, retorna a mesma string adicionada do caractere "#" no início, no meio e no final dela
    str -> str'''
    return '#'+s[0:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'