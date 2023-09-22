def hashtag(s):
    '''dada uma string (s), retorna o caractere # no inicio, no meio e no final dela
       : str -> str
    '''
    s = str('#' + str(s[0:((len(s))//2)]) + '#' + str([((len(s))//2):]) + '#')