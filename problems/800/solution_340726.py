# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
#
#
def total(lista,dic):
    i=0
    s={0}
    while i<len(lista):
        if lista[i] in dic:
            s=s+dict.values(lista[i])
        i=i+1
    return s