def hashtag(s):
    '''Função que recebe uma string (s) 
       qualquer e adiciona um carctere '#' 
       no começo, no meio e no final dela. 
       str -> str'''
    
    comeco = s[0]
    meio = str(len(s)// 2)
    fim = len(s)
    
    return '#' + comeco + s[comeco:meio] + '#' + meio + s[meio:fim] + '#' + fim + '#'