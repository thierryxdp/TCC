def lingua_p(palavra):
    '''recebe e retorna a palavra na lingua do p, ou seja, com um p inserido antes de cada vogal
    str -> str'''
    
    pv = ''
    
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            pv = pv + 'p' + palavra[i]
        else:
            pv = pv + palavra[i]
            
    return pv