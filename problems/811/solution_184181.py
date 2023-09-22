# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(med,H,L):
    '''criando um if para a altura se o colchão tiver uma altura
    maior que a largura, se tivermos o contrário caimos no else'''
    if H>L:
        return med[0]<= L and med[1]<= H
    else:
        return med[0]<= H and med[1]<=L