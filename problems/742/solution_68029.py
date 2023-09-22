def substitui(s:str,x:str,i:int) ->str:
    """
    recebe uma string e retorna a mesma string, apenas
    trocando um de seus elementos por um termo em um
    determinado indice, fornecidos a string, o indice
    a ser substituido e o termo novo
    """
    return s[0:i] + str(x) + s[i+1:]