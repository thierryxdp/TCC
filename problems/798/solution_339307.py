# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    lista_palavras=frase.split()
    dicio={}
    for i in lista_palavras:
        if i not in dicio:
            dicio.update({i:lista_palavras.count(i)})
    return dicio