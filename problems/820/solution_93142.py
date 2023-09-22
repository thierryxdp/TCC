def posLetra(string, letra, n):
    """Função que dada uma string e uma letra, retorna a posição da ocorrência 'n' da
    letra na string e retorna -1 se o número de ocorrências for menor que o número dado;
    string, string, int -> int"""
    if string.count(letra) >= n:
        i=0
        aparicao=0
        while i<len(string):
            if string[i] == letra:
                    aparicao+=1
                    if aparicao == n:
                        return i
            i+=1
    else:
        return -1