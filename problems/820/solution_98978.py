def posLetra (string,letra,n):
    '''recebe uma string, uma letra e um número que indica a ocorrência dessa letra, e retorna a posição da string em que a letra está'''
    '''str, str, int -> int'''
    teste = str.count(string,letra)
    teste2= str.find(string, letra, n)
    if teste <1:
        return -1
    else:
        
    if teste >=1:
        return teste2