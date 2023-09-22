def posLetra(texto,letra,numero):
    """A função retorna em que opsição da string daquela ocorrência
    da letra se encontra ou retornar -1 caso exista menos ocorrência
    da letra do que a ocorrência pedida.
    str--str--int-->int."""
    
    i = 0
    ocorrencias = 0
    while i < len(texto):
        if letra in texto[i]:
            i += 1
            if ocorrencia == numero:
                return i
        i += 1
    if numero > ocorrencias:
        return -1
    else:
        return ocorrencias