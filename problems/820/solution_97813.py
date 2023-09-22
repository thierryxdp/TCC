def posLetra(string,letra,n):
    """Recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada
    da letra e retorna em que posição da string aquela ocorrência da letra está;
    str,str,int->int"""
    contador=0
    ocorrencia=-1
    while contador<len(string):
        if letra in string[contador]:
            ocorrencia=ocorrencia+1
        elif ocorrencia==n:
            return contador
        contador=contador+1