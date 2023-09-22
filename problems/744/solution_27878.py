'''função que recebe uma string e insere '#' no início, meio e final dela.
    a string (s) deve, obrigatoriamente, ser indicada entre aspas.
    str -> str'''
def hashtag(s):
    meio=len(s)//2
    return '#'+s[:meio]+'#'+s[meio:]+'#'