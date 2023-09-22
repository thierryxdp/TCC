def posLetra(string,letra,numero):
    """A função recebe uma string, uma letra e um número que
    indicará a ocorrência desejada da letra. A função retornará
    
    Entrada: String, String, Int
    Saída: Int"""
    
    ocorrencia=-1
    string_rev= (string[::-1])
    
    while str.count(string,letra) >= numero:
        ult_repeticao = str.index(string_rev,letra)
        ocorrencia = 1 + ult_repeticao
    
    return string_rev