def posLetra(string,letra,n):
    """funçao que recebe como entrada uma frase, uma letra e um numero que indica a ocorrencia desejada da letra dentro da frase,
    e retorna a posição na string daquela ocorrencia desejada;
    str,str,int-->int"""
    ocorrencia = str.count(string,letra)
    ocorre = 0
    i = -1
    if n == ocorrencia:
        return string.rfind(letra)
    elif 0 < n < ocorrencia:
        while ocorre != n:
            i = i+1
            if (string[i] == letra):
                ocorre = ocorre+1
        return i
    elif not(0 < n <= ocorrencia):
        return -1