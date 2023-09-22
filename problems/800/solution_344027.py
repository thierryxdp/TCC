# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls,dc):
    
    s=0
    for x in ls:
        s=s+dc[ls]
    return round(s,2)