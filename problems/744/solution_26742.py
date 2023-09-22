from math import*
def hashtag(s):
    '''funcao que dado uma string retorna o caractere '#'
    no inicio,meio e final da string; str -> str'''
    if len(str)%2==0:
        x = len(str(s))/2
        return '#' + str(s)[0:x] + '#' + str(s)[x:] + '#'
    else:
        y = math.ceil(len(str(s))/2)
        return '#' + str(s)[0:y] + '#' + str(s)[y:] + '#'