def conta_frase(frase):
    '''Função que retorna o número de palavras de uma frase.
    Entrada: str. Saída: int. '''
    lista = str.split(frase,' ')
    return len(lista)