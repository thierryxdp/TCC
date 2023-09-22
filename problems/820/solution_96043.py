def posLetra(string,l,n):
    """Função que recebe uma string, uma letra e um número inteiro
       que indica a ocorrência desejada da letra
       Parâmetros de entrada:str,str,int
       Parâmetros de saída:int"""
    if str.count(string,l)<n:
        return '-1'
    i=0
    n=0
    else: 
        return str.index(string,l,n)