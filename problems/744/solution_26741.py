def hashtag(s):
    '''funcao que dado uma string retorna o caractere '#'
    no inicio,meio e final da string; str -> str'''
    x = len(str(s))/2 
    return '#' + str(s)[0:x] + '#' + str(s)[x+1:] + '#'