Freq_palavras(frases):
    """Retorna a frequencia das palavras do texto"""
    texto = frases.split()
    frequencia = []
    for palavra in texto:
       frequencia.append(texto.count(palavra))
    contador = {}
    for palavra in range(len(texto)):
        contador[texto[palavra]] = frequencia [palavra]
    return contador