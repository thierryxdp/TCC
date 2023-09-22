def posLetra(string,string_procurada,n):
    contador = 0
    posicao = 0
    a = str.count(string, string_procurada)
    if a < n:
        return -1
    else:
        while posicao <= a - 1:
            if string[contador] == string_procurada:
                posicao = posicao + 1
            contador = contador + 1
        return posicao