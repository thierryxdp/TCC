# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(S1,H,L):
    '''Função que recebe uma lista "S1" com as dimensões da cama e dois
    inteiros "H" e "L" que são dimensões da porta, e calcula a possibilidade
    do colchao passar pela porta, retornando "True" caso passe e "False"
    caso não passe'''
    '''list, int, int -> bool'''
    #Casos de teste:
    ''' colchao([500,700,400],500,250) -> False
        colchao([50,240,440],400,200) -> True
        colchao([25,300,200],250,150) -> True '''
    A,B,C=S1[0],S1[1],S1[2]
    S1=sorted([A,B,C]) #sorted é utilizado para colocar em ordem crescente
    P1=sorted([H,L])
    if (S1[0]<=P1[0]) and (S1[1]<=P1[1]):
        return True
    else:
        return False