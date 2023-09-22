def posLetra(frase,letra,n):
    """função que retorna em qual posição a ocorrência da letra está, através da frase de entrada
    letra e n referente a ocorrência desejada;
    Entrada: str, str, int
    Saída: int"""
    i = 0
    inicio = 0
    resposta = 0
    
    while i<n:
        inicio = str.find(frase,letra,inicio) + 1
        resposta = inicio - 1
        i = i + 1
    return resposta