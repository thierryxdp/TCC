# Dada uma string, uma letra e um número n, 
# queremos a posição na string da letra em sua
# n-ésima ocorrência.
# Resolução:
# 1. Se não há n ocorrências da letra na string, posição = -1;
# 2. Analisar cada elemento da string e marcar quando for igual à letra;
# 3. Parar quando existir n letras marcadas ;
# 4. Devolver a posição i do elemento em que (3) for concluído.

def posLetra(string: str, letra: str, n: int) -> int:
    '''Dada uma string, uma letra e um número n, 
    devolve a posição na string da letra em sua
    n-ésima ocorrência'''
    posicao = 0
    ocorrencia = 0
    if str.count(string, letra) < n:
        posicao = -1
    while (ocorrencia < n):
        if string[posicao] == letra:
            ocorrencia += 1
        posicao += 1
    return posicao