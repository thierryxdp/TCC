def hashtag(s):
    '''funcao que insere o cacactere '#' no inicio,meio e final de uma string; str -> str'''
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'