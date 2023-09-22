def posLetra(string,letra,n):
    """Função que retorna a posição de uma letra na string dada o número de ocorrências
caso haja menos ocorrências do que solicitado a função retorna -1;
str, str, int -> int"""
    posicao= string.find(letra)
    while posicao>=0 and n>1:
        posicao= string.find(letra,posicao+1)
        n-=1
    return posicao