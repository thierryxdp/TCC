# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    div_str= len(s)//2
    
    return '#' +s[:div_str]+ '#' +s[div_str:] +'#'