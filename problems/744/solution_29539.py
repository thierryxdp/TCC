def hashtag(s):
    '''recebe uma string s e insere o caractere x no início,
    no meio e no final dela
    str->str'''
    string=s
    meio=len(s)//2
    if len(s)%2==0:
        return '#'+s[:meio]+'#'+s[meio:]+'#'
    else: