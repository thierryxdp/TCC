def posLetra ( string, letra, numero):
    """essa função irá retornar a posição da string em que aquela ocorrencia da letra está ; string -> int"""
    c = 0
    aux = 1
    
    while c < len (string):
        if string [c] == letra:
            aux += 1
            
        if aux == numero:
            return c
        
	return -1