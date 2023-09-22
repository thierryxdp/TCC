def posLetra(string, letra, n):
    """Recebe como entrada uma string, uma letra e um número, que indica
a ocorrência desejada da letra, e retorna em qual posição da string aquela letra
está sendo que, em caso de menores ocorrências do que o pedido retorna-se -1;
str, str, int -> int"""
    proximo = 0
    posicao = ()

    if str.count(string, letra) < n:
        posicao = -1
        
    else:
        while proximo <= n:
            if letra == string[proximo]:
                posicao = proximo  
            proximo = proximo + 1
   
    return posicao