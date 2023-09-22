# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, produt):
    soma=0
    x=0
    while x<len(lista):
        soma+=produt[lista[x]]
        x+=1
    return round(soma, 2)