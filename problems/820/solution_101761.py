def posLetra(string,letra,numero):
    """Dada uma string, uma letra e o número de ocorrências
    desejada dessa letra, a função retorna a posição de ocorrência
    que a letra está e caso exista menos ocorrências do que a
    desejada, a função retorna -1.
    Parametros de Entrada: str,str,int
    Retorna: int"""

    i=0
    contador=0
    
    while i< len(string):
        if string[i]in letra:
            contador= contador+ 1
            if contador==numero:
                return i
        i=i+1
    if numero>contador:
        return -1