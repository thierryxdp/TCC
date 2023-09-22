def posLetra(string,letra,numero):
    """Dada uma string, uma letra e um número retornará em que posição da string a letra está
       de acordo com a ocorrência pedida representada pelo número.
       str, str, int -> int"""
    
    posicao = 1
    
    while posicao <= len(string):
        if string[posicao] in letra:
            posicao += 1