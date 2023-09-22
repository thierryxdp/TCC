def posLetra(texto, caracter, ocorrencia):
    """
    Retorna a posição de certa ocorrência de uma letra, se contida em uma string.
    Retorna -1, caso a ocorrência informada seja menor do que a presente no texto.
    str, str, int -> str

    Parameters:
    texto: Parâmetro textual, do tipo string (str);
    caracter: Parâmetro textual, do tipo string (str);
    ocorrencia: Parâmetro numérico, do tipo inteiro (int);
    
    Returns:
    A posição de determinda occorrência de uma letra em um texto.
    """
    
    i = 0
    indices = []
    posicoes_caracter = []
    posicao = 0
    removido = 0
    tamanho = len(texto)

    while caracter in texto:
        posicao = texto.find(caracter)

        if i == 0:
            list.append(posicoes_caracter, posicao)
            
        else:
            texto = texto[posicao + 1:]
            novo_tamanho = (len(texto))
            indices.append(tamanho - novo_tamanho - 1)           
        i = i + 1

    if ocorrencia > len(indices):
        posicao = -1
    else:
        posicao = indices[ocorrencia - 1]

    return posicao