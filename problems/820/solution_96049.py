def posLetra(string,l,n):
    """Função que recebe uma string, uma letra e um número inteiro
       que indica a ocorrência desejada da letra
       Parâmetros de entrada:str,str,int
       Parâmetros de saída:int"""
    if str.count(string,l)<n:
        return '-1'
    else:
        x=str.replace(string,l,' ',n-1)
        return str.index(x,l)