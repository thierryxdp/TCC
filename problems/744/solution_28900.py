def hashtag(s):
    '''retorna a string s concatenanda com o caractere # no início, meio e final; str->str'''
    if len(s)%2==0:
        return '#'+s[0:len(s)/2]+'#'+s[len(s)/2:0]+'#'