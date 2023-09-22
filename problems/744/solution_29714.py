def hashtag(s):
    '''Fazer uma funcao que receba uma string e retorne # no inicio,meio e final dela;
    str -> str'''
    
    meio = len(s)//2
    
    return '#' + str (s[0:meio]) + '#' + str (s[meio:]) + '#'