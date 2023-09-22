def posLetra(texto,letra,ocorrencia):
    """Função que identifica e retorna a posição da ocorrência de uma letra em
um texto dado.
    str, str, int -> int"""
    
    if str.count(texto,letra) < ocorrencia:
        indice = -1

    elif letra in texto:
        ocorrencias = ['']
        texto = list(texto)
        
        while len(ocorrencias) < ocorrencia:
            list.remove(texto,letra)
            list.append(ocorrencias,letra)

        indice = list.index(texto,letra) + (len(ocorrencias) - 1)
                 
    else:
        indice = -1
        
    return indice