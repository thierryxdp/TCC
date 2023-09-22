# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    ''' função que mostra quantas vezes cada palavra se repete
    string -> dict'''
    palavras = frases.split()
    lista = {}
    for i in range(len(palavras)):
        lista[palavras[i]] = palavras.count(palavras[i])
        
    return lista