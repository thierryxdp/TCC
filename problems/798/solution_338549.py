# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    ''' str > dict
    Recebe uma frase e retorna a quantidade de vezes que cada
    palavra aparece dentro dela'''
    
    frase = str.split(frases, ' ')
    freq = {}
    
    for p in frase:
        freq[p] = list.count(frase, p)
    return freq