def conta_frases(frase):
    "A questão irá contar o númerdo de frases no texto passado pela variável frase"
    "Entrada: Strin | Saída: Inteiro"
    ponto = frase.replace('!', '.').replace('?', '.').replace('...', '.')
    lista = ponto.split('.')
    return len(lista) - 1