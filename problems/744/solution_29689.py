def hashtag(s):
    '''Função que recebe uma string (s) 
       qualquer e adiciona um carctere '#' 
       no começo, no meio e no final dela. 
       str -> str'''
    
    comeco = s[0]
    meio = len(s) + s[0] // 2
    fim = len(s)
    
    return '#' + comeco + s[:meio] + '#' + meio + s[:fim] + '#' + fim + '#'