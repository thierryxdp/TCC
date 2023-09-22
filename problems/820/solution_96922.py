def posLetra(string, letra, numero):
    '''Retorna a posição da string em qual ocorrência da letra recebida
    está, caso n, caso não encontrda retorna -1 
    string, string int -> int'''
    indice = 0
    ocorrencia = 0
    indice_ocorrencia = 0
    while indice < len(string):
        if string[indice] == letra:
            ocorrencia += 1
            indice_ocorrencia = indice
        indice += 1   
    if ocorrencia == numero:
           return indice_ocorrencia 
        
    else:
        return -1