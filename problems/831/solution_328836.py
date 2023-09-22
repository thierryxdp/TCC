def lingua_p(palavra):
    """Funcao que, dado uma palavra de entrada, retorna essa mesma palavra traduzida para a lingua do P.
    Para traduir para a lingua do P, basta introduzir, a cada vogal da palavra original, a letra 'p' mais a vogal origem,
    ignorando a diferenca entre minusculos e maiusculos, retornando a palavra traduzida toda em minusculo;
    str -> str"""
    string_saida=''
    for indice in range(len(palavra)):
        if palavra[indice]in'AEIOUaeiouáéíóú':
            string_saida+=palavra[indice]+'p'+str(palavra[indice])
        else:
            string_saida+=palavra[indice]
    return string_saida.lower()