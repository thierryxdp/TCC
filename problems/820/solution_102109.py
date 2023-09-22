def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra;
    retornando a posição da string que aquela ocorrência da letra está;
    str, str, int -> int'''
    i=0
    posicao=string.find(letra)
   
    while i<len(string):
        if posicao>=0 and numero>1:
            posicao=string.find(letra, posicao+1)
            
        i+=1
    return posicao