# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(a,b,c,h,l):
    colchao = (a,b,c)
    porta = (h,l)
    if max(porta)>max(colchao):
        return True
    if max(porta)<max(colchao):
        return False
    if max(porta)==max(colchao):
        return True