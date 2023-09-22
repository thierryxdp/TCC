# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
#
#
def total(l,d):
    i=0
    s={}
    while i<len(l):
        if l[i] in d:            
            s=dict.values(l[i])
        i=i+1
    return s