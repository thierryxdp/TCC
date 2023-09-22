def inverte(frase):
    """A função dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entredan orddem inversa.
    Assinatura: str -> str"""
    if '-' or ',' or '.' in frase:
        virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    return str.reverse(ponto_final)
    if '?' in frase:
            virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    return str.reverse(ponto_interrogacao)
    
    if '!' in frase:
            virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    return str.reverse(ponto_exclamacao)