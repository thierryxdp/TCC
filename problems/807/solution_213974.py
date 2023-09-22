def conta_frase(texto):
    '''Funcao que retorna a quantidade 
    de frases de um dado texto.
    Dados de entrada: str
    Valor de saida: int
    '''
    total_frases=0
    for i in range(len(texto)):
        if i > 0 and texto[i - 1] == ".":
            continue 
        if texto[i] in (".", "!", "?"):
            total_frases += 1 
    return total_frases