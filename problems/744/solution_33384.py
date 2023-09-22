# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
        '''
    Função que recebe uma string e insira o caractere "#" no
    inicio, no meio de no final dela
    '''
    x=len(s)
    y=x
    
    return str("#")+s[0:y]+str("#")+s[x:]+str("#")