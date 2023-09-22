def posLetra (frase,letra,numero):
    """função que dada uma string, letra e numero, retorne em 
    que posição da string aquela letra está dada a ocorrência"""
    """str, str, int -> int"""
        posLetra = frase.find(letra)
        while posLetra >= 0 and numero > 1:
            posLetra = frase.find(letra, pos +1)
            numero -= 1
        return posLetra