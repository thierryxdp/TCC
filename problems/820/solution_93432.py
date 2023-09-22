def posLetra (string, letra, número):
    """Função que, dada uma string, uma letra e um número que indica a ocorrência desejada da letra, retorna a posição da ocorrência daquela letra na string. Caso exista menos ocorrências da letra do que a pedida, deve retornar -1
    entrada: str, str, int
    saída: int"""
    
    proximo = 0
    
    while proximo < len(string):