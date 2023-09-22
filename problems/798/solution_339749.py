# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = str.split(frases)
    list_freq = {}
    contagem = 0
    limit = len(palavras)
    
    while contagem < limit:
        list_freq[palavras[contagem]] = palavras.count(palavras[contagem])
        contagem += 1 
    return list_freq
'''funçao'''