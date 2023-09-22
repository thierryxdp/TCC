def posLetra(string, letra, numero):
    '''Retorna a posição da string em qual ocorrência da letra recebida
    está, caso n, caso não encontrda retorna -1 
    string, string int -> int'''

    indice = 0
    ocorrencia = 0
    indice_ocorrencia = 0
    while indice < len(string):
        if letra == string[indice] and numero == str.count(string,letra, 0, indice+1):
            ocorrencia += 1
            indice_ocorrencia = indice
            return indice_ocorrencia
        indice += 1
   
    return -1