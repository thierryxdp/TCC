# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls,dc):
    '''Calcula o valor de uma compra.
    Assinatura: ls,dc->float'''
    s=0
    for x in ls:
        s=s+dc[x]
    return round(s,2)