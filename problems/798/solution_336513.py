def freq_palavras(frases):
    """Retorna a frequencia da palvra em um texto
       str-> dict"""
    contagem = {}
    lista = str.split(frases)
    for palavra in lista:
        contagem[palavra] = list.count(lista, palavra)
    return contagem