def posLetra(string,letra,numero):
    """A função recebe uma string, uma letra e um número que
    indicará a ocorrência desejada da letra. A função retornará
    
    Entrada: String, String, Int
    Saída: Int"""
    
    ocorrencia=-1
    
    while str.count(string,letra) >= numero:
        ocorrencia = str.index(string,letra,numero)
         
    return ocorrencia