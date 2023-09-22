def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
       onde cada palavra dessa string seja uma chave e tenha
       como valor o número de vezes que a palavra aparece;
       string -> dict"""
    palavra = ''
    dicionario = {}
    for letra in frases:
        if letra != '':
            palavra = palavra + letra
            numero_vezes = str.count(frases,palavra)
        elif letra == '':
            palavra = ''
            dicionario[palavra] = numero_vezes
    return dicionario