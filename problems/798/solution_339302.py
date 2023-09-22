# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    lista_palavras=frase.split()
    dicio={}
    for i in lista_palavras:
        palavra=lista_palavras[i]
        if palavra not in dicio:
            dicio.update(palavra,frase.count(palavra))
    return dicio