def posLetra(frase,letra,numero):

    """ Nesta função, queremos que nos retorne a posição da letra após ela
        aparecer na frase na quantidade de vezes representada pelo numero
        fornecido pela função. Após uma letra aparecer 'número' vezes, a função
        while acaba e a função retorna a posição desta letra.

        str,str,int -> int
    """

    i = 0
    contador = 0

    while i < len(frase)-1:
        if (frase[i] == letra):
            contador = contador + 1
        i = i + 1
    return i