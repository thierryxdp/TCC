def posLetra(texto,letra,n):
   '''
Função que recebe como entrada uma string,uma letra, e
um número n que indica a ocorrência da letra desejada e
retorna a posição da string em que a ocorrência da letra está.

str,str,int-->int
    '''

    i=n
    pos=-1
    while i>0:
        pos=str.find(texto,letra,pos+1)
        i=i-1
        if pos==-1:
            return -1
    return pos