def posLetra(string,letra,numero):
    """A função recebe uma string, uma letra e um número que
    indicará a ocorrência desejada da letra. A função retornará
    Entrada: String, String, Int
    Saída: Int"""
    
    ocorrencia=-1
    i=0
    while string.count(letra) >= numero:
        ocorrencia=ocorrencia+2
    return ocorrencia