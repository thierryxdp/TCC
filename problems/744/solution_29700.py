def hashtag(s):
    '''Função que recebe uma string (s) 
       qualquer e adiciona um carctere '#' 
       no começo, no meio e no final dela. 
       str -> str'''
    
    meio = len(s) // 2
    fim = len(s) + 1
    
    return '#' + s[0:meio] + '#' + s[meio:fim] +'#'