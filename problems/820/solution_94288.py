def posLetra(string, letra, numero):
    """
    	Função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra.
        A função retorna em que posição da string aquela ocorrência da letra está.
        Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1.
        str, str, int -> int
    """
    
    i = 0
    num_ocorrencia = 0
    
    while i<len(string) and num_ocorrencia<numero:
        
        if string[i] == letra:
            num_ocorrencia = num_ocorrencia + 1
        i = i + 1
        
    if num_ocorrencia < numero:
        return -1
    
    else:
        return i-1