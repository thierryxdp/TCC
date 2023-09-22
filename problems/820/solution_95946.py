def posLetra(frase, letra, ocorrencia):
    """ Indica a posição da string onde esta localizada a ocorrênia desejada da letra desejada.
    	str, str, int -> int
        
        Parameters:
        frase: Frase
        letra: Letra
        ocorrencia: Ocorrência
        
        Returns: A osição da string onde esta localizada a ocorrênia desejada da letra desejada.
    """
    if frase.count(letra) < ocorrencia:
        return -1
    elif frase.count(letra) >= ocorrencia and ocorrencia == 1:
        return frase.find(letra)
    elif frase.count(letra) >= ocorrencia and ocorrencia > 1:
        vez = frase.find(letra)
        while ocorrencia > 1:
            vez = frase.find(letra, vez + 1)
            ocorrencia = ocorrencia - 1
        return vez