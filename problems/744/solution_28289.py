def hashtag(s):
    '''funcao que recebe uma string e retorna a mesma string str->str'''
    return '#' + s[:len(s)//2:] + '#' + s[len(s)//2:] + '#'