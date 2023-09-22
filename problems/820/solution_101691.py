def posLetra(string,letra,n):
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