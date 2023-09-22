# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string (s) e retorna a modificação dessa string com 
    hashtags ("#") no ínicio, meio e fim dela'''
    inicioString = s[:len(s)//2]
    fimString = s[len(s)//2:]
    
    return "#"+inicioString+"#"+fimString+"#"