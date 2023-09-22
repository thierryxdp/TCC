def posLetra(frase,letra,n):
    """
    Função recebe como entrada uma string(frase), uma letra, e um número que indica
    a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc). 
    Retorna em que posição da string a ocorrência da letra está. Caso exista menos
    ocorrências da letra do que a ocorrência pedida, a função retorna -1.
    """
    i=0
    repeticoes=""
    while i<len(frase):
        if frase[i]==letra:
            repeticoes+=frase[i]
            i+=1
        else:
        	i+=1
        if len(repeticoes)==n:             
            return i-1
    if len(repeticoes)<n:
        return -1