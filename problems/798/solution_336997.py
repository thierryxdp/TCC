def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra
    dessa string seja uma chave  e tenha  como valor o número de
    vezes que a palavra acontece
    str-->dic"""
    palavras = frases.strip()
    ocorrencias = frases.count(palavras)
    for palavras in frases:
        dicionario [palavras] = [ocorrencias]
        return dicionario