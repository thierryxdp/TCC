def posLetra (string, letra, numero):
    """Função que retorna em qual posição da string a ocorrencia
    da letra está.
    str, str, int -> int"""
    
    indice = 0
    ocorrencia = 0
    
    while indice < len(string):
        
        if string [indice] == letra:
            ocorrencia += 1
            
            if ocorrencia == numero:
                return indice
        
        indice += 1
        
        else:
            return -1