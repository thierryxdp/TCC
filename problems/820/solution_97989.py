def posLetra(string, letra, num):
    
    
    """Dada uma string uma letra e um numero que
    corresponde a ocorrencia da letra, calcula a
    posição desta ocorrência. str, str, int -> int """
    
    lista = list (string)
    cont = lista.count(letra)

    if cont >= num:
        
        sub = str.replace(string, letra, '&', num - 1)
        return str.find(substitui, letra, 0, -1)
    else:
        return -1