def freq_palavras(frases):
    '''retorna a frequencia que cada palavra aparece na frase
    str --> dict'''
    lista_palavras=str.split(frases)
    ocorrencia_palavras={}
    for palavra in lista_palavras:
        ocorrencia_palavras[palavra]=list.count(palavra)
    return ocorrencia_palavras