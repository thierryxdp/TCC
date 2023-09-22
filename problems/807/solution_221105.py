def conta_frases(frase, palavra, pos1, pos2):
    """Faca uma funcao que dada uma frase, uma palavra, e duas posicoes,
    retorna a frase excluindo-se as ocorrencias desta palavra entre estas duas 
    posicoes, inclusive"""
    index = str.find(frase, palavra, pos1, pos2)
    size = len(palavra)
    if (not index == -1) and (pos1 + index + size < pos2):
        pos2 -= index + size - 1
        return frase[:index] + retirar(frase[index + size:], palavra, 0, pos2)
    else:
        return frase[:index] + frase[index + size:]