def hashtag(s):
    '''funcao que retorna o caractere'#'no inicio,meio e final de uma funcao
    str->str'''
    s='#'+ s[:len(s)%2]+'#'+s[len(s)%2:]+'#'
    return s