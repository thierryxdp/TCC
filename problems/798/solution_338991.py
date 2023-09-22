# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''função em que dada uma string, retorne um dicionário onde 
    cada palavra dessa string seja uma chave e tenha como valor o número
    de vezes que a palavra aparece list -> dici'''
    dici = [] 
    for palavra in frases:
        if frases in palavras[palavra]:
            dici = dici + [palavra]
    return dici