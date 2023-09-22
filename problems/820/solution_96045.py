def posLetra(string,l,n):
    """Função que recebe uma string, uma letra e um número inteiro
       que indica a ocorrência desejada da letra
       Parâmetros de entrada:str,str,int
       Parâmetros de saída:int"""
    i=0
    n=0
    while i<len(string):
        if str[i]==n:
            return i
        indice=indice+1
    return -1