# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funcao que recebe uma string e insere o caractere 
    # no inicio, meio e fim da string.
    assinatura: str -> str
    '''
    meio = (len(s)//2)
    str_Alterada3 = str('#')+s[:meio]+str('#')+s[meio:]+str('#')  
    return str_Alterada3