# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Funcao que recebe uma string e coloca uma '#' 
    no inicio, meio e fim da string
    
    str-> str
    '''
    meio = len(s)//2
    return '#' + s[0:meio] + '#' + s[meio:len(s)]]