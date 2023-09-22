# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = str.split(frases)
    list_freq = {}
    conta = 0
    limit = len(palavras)
    
    while conta < limit:
        list_freq[palavras[conta]] = palavras.count(palavras[conta])
        conta += 1 
    return list_freq