def posLetra(texto,letra,ocorrencia):
    """Função que identifica e retorna a posição da ocorrência de uma letra em
um texto dado.
    str, str, int -> int"""

    if letra in texto:
        ocorrencias = ['']
        texto = list(texto)
        
        while len(ocorrencias) < ocorrencia:
            list.remove(texto,letra)
            list.append(ocorrencias,letra)

        indice = list.find(texto,letra) + (len(ocorrencias) - 1)
                 
    else:
        indice = -1
        
    return indice