# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lis,pro):
    i=0
    to=0
    while i<len(lis):
        to=to+pro[lis[i]]
        i=i+1
    return to