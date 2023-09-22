def posLetra(frase,x, n):
    """funçao que recebe uma frase, uma letra x e a ocorrencia n desejada da letra na frase e retorna a posiçao da ocorrencia caso n seja menor que o numero de ocorrencias na frase retorna -1.
    entrada: str, str, int;
    saida: int."""
    
    totaldeocorrencia = str.count(frase, x)
    if n > totaldeocorrencia:
        return -1