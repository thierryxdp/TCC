def posLetra(frase,letra,num):
    '''
    	Função que recebe entrada uma string, uma letra, 
        e um número que indica a ocorrência desejada da letra, e 
        retornar em que posição da string aquela ocorrência da letra está.
        OBS:Caso exista menos ocorrências da letra do que a 
        ocorrência pedida, a função deve retornar -1.
        contador:int
        i:int
        res:int
        frase:str
        letra:str
        num:int
    '''
    contador = 0
    i=0
    res = -1
    while i < len(frase):
        if frase[i] == letra:
           contador += 1
        if contador == num:
            res = i
            contador += 1
        i+=1
    return res