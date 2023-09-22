# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(med,h,l):
    if (med[0]<h and med[1]<l) or (med[1]<h and med[0]<l):
        return True
    else:
        return False