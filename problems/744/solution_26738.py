def hashtag(s):
    '''funcao que dado uma string retorna o caractere '#'
    no inicio,meio e final da string; str -> str'''
    return '#' + str(s)[0:len(str(s))/2 -1] + '#' + str(s)[len(str(s))/2:] + '#'