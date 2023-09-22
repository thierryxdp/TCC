def posLetra( string, letra , numero):
    """ Função que dada uma string, uma letra e um numero retorna a posição da string 
    onde a letra está. Caso exista menos ocorrências da letra a função retorna -1
    parametro: str, str , int --> int"""
    i = 0
    contador = 0
    while i < len (string) -1:
        if string [ i ] == letra:
            contador = contador + 1
        if contador == numero :
            return i 
        i = i + 1
    return -1