def hashtag(s):
    '''
    função recebe uma string e retorna 
    a mesma tendo uma "#" no inicio, no meio 
    e no fim. 
    '''
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'