def freq_palavras(frases):
    "função recebe frase e retorna dicionário com quantidade de cada palavra da string str--> dict""
    palavras = str.split(frases)
    list_freq = {}
    contagem = 0
    limit = len(palavras)
    
    while contagem < limit:
        list_freq[palavras[contagem]] = palavras.count(palavras[contagem])
        contagem += 1 
    return list_freq