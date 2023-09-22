def posLetra(string, letra, num):
    """ Função que recebe uma string, um número e uma letra, retorna a posição que essa letra está de acordo com a sua ocorrência.
   	 str, str, int - > int  """
    
    c = 0
    ind = 0
    ocorrencia = 0
    lista = list(string)
    while c < len(lista):
        if lista[ind] == letra:
            ocorrencia += 1
            if ocorrencia == num:
                return ind
            
            c += 1
            ind += 1
            return -1