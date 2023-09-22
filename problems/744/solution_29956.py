def hashtag(s):
    '''funcao que insere o cacactere '#' no inicio,meio e final de uma string; str -> str'''
    return  '#' + [0:len(s)//2] + '#' + [len(s)//2:] + '#'