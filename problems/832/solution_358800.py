#Entrada: Uma matriz
#1 - Precisamos analisar se a matriz é quadrada ou não
#2 - Uma matriz quadrada tem o número de linhas e colunas iguais
#3 - Preciamos comparar o numero de linhas e colunas 
#4 - Se for igual, retornamos true, se não retornamos False
def eh_quadrada(m: list) -> bool:
    """A função recebe uma matriz 
    e diz se ela é quadrada ou não"""
    if len(m)== len(m[0]):
        return True
    else:
        return False