# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(lista,H,L):
    """Função que recebe uma lista de tamanho 3; a altura 'H' e a  
       largura 'L' da porta e informa se o colchão passará ou não pela porta
       parâmetros de entrada:list,int,int
       parâmetros de saída:bool"""
    A=lista[0]
    B=lista[1]
    C=lista[2]
    if ((A>H) and (B>H) and (C>H)) and ((A>L) and (B>L) and (C>L)):
        return True
    else:
        return False