def posLetra (frase, letra, numero):
    """Função que dada uma frase, uma letra e um numero que indica a ocorrencia, retorna a posição que aquela ocorrencia da letra ocupa na frase;
    str, str, int -> int."""
    frasenova= str.lower (frase)
    quantidade= str.count (frase, letra)
    if letra not in frase or numero > quantidade:
        return -1
    i=0
    j=0
    while i < len (frase):
        if frase [i] == letra:
            j= j+1
        if j== numero:
            return i
        i= i+1