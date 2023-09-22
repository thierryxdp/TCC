def posLetra(frase,letra,num):
    '''
    	Função que recebe como entrada uma string, uma letra,
        e um número que indica a ocorrência desejada da letra,
        retornando em que posição da string aquela ocorrência da letra está.
        OBS:Caso exista menos ocorrências da letra do que a ocorrência pedida,
        a função deve retornar -1.
        i:int
        frase:str
        letra:str
        num:int
        
    '''
    contador = 0
    i=0
    while i < len(frase):
        if frase[i] in letra:
           contador += 1
        i+=1
    if contador < num:
        contador = -1
        return contador
    return contador, 'posição da '+ str(num) +' ocorrência da letra '+ (letra) +' na string dada'