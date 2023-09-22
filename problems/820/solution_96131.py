def posLetra(texto: str, letra: str, ocorrencia: int) -> int:
    """Retorna a posição da letra indicada na entrada no texto dado
       pelo parâmtro texto, em sua ocorrência indicada no parâmetro 
       ocorrencia."""
    
    ocorrencias = 0
    i = 0
    
    while (i < len(texto) and ocorrencias < ocorrencia):
        if (texto[i] == letra):
            ocorrencias += 1
            
        i += 1
       
    if (ocorrencias < ocorrencia):
        return -1
    else:
    	return i