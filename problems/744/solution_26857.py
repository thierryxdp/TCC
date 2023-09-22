'''Após inserida pelo usuário uma string, o programa a retorna com "#"'s 
no início, meio e fim. str-> str'''
def hashtag(s):
    comprimento = len(s)
    compr = len(s)//2
    parte1 = s[0:compr]
    parte2 = s[compr:comprimento]
    return '#' + parte1 + '#' + parte2 + '#'