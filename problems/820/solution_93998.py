def posLetra(string, letra, ocorrencia):
   	""" Funcao que recebe uma string e retorna a posicao onde uma
    ocorrencia especifica aparece.
    Entrada: str, str, int;
    Saida: int;
    
    Parameters:
    string: string que sera verificada;
    letra: letra para ver as ocorrencias;
    ocorrencia: numero da ocorrencia da letra.
    """
    seguinte = 0
    lugar = []
    if string.count(letra) < ocorrencia:
        return -1
    while seguinte < len(string):
        if string[seguinte] == letra:
            lugar.append(seguinte)
        seguinte = seguinte + 1
    return lugar[ocorrencia - 1]