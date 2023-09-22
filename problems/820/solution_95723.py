def posLetra(string,letra,num):
    """Mostra a posição da ocorrência desejada da letra
    	str, str, int -> int
        Parameters:
        string: String a ser analisada
        letra: Letra que se deseja encontrar
        num: Número de ocorrência desejada da letra
        
        Returns:
        A posição da ocorrência desejada da letra fornecida
    """
    
    i = 0
    ocorrencia = 0
    
    while i < len(string):
        if string[i] == letra:
            ocorrencia = ocorrencia + 1 
            if ocorrencia == num:
                return string.index(string[i], indice)
        i = i + 1
    else:
        return -1