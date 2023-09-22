# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = str.split(frases)
    lista_freq = {}
    contador = 0
    limite = len(palavras)
    
    while contador < limite:
        lista_freq[palavras[contador]] = palavras.count(palavras[contador])
        contador += 1 
    return lista_freq