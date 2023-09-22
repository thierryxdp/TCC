def freq_palavras(frases):
    '''retorna um dicionario com as palavras e a qnt de vezes que se repetem'''
    nova = []
    freq = []
    for palavra in frases:
        if palavra not in nova:
            nova.append(palavra)
            set freq = 1
        else:
            increase freq