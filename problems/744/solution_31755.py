# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''
    Função que recebe uma string s e insere o caractere
    # no inicio, no meio e no final dela.
    str-> str
    '''
    
    n=(len(s)-1)/2
    p1=s[:(n)+1)]
    p2=s[(n)+1):]
    
    
    return "#"+p1+"#"+p2+"#"