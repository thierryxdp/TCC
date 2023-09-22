def posLetra(frase,letra,numero):
    """funcao que recebe uma str, uma letra e um numero que indica a ocorrencia desejada da letra e retorna um int dizendo em que posicao isso ocorre.
    str,str,int->int."""
    x=1
    if str.count(frase,letra)<numero:
        return -1
    while x!=numero:
        frase=str.replace(frase,letra," ",1)
        x=x+1
    return str.index(frase,letra)