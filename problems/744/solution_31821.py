# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    A função recebe uma string e retorna com '#' no inicio,
    no começo e no fim; string--> string
    '''
    
    div_str= len(s)//2
    
    return '#' +s[:div_str]+ '#' +s[div_str:] +'#'