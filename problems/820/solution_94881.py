def posLetra(string,letra,numero):
    """Dada uma string, uma letra e um número retornará em que posição da string a letra está
       de acordo com a ocorrência pedida representada pelo número.
       str, str, int -> int"""
    
    contador = 0
    posicao = 0
    
    while True:
        if string(numero) == letra:
            posicao = posicao + 1
            contador = contador + 1
            return string[posicao]