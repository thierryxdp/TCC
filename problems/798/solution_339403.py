def freq_palavras(frases):
    '''Esta função conta o número de palavras repetidas
    em um texto
    assinatura str -> str'''
    texto = frases.split()
    frequencia = []
    for palavra in texto:
        frequencia.append(texto.count(palavra))
    contador = {}
    for quantidade in range(len(texto)):
        contador[texto[quantidade]] = frequencia[quantidade]