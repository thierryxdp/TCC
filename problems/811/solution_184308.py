# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Funcao que retorna se o colchao consegue ou não passar
    pela porta, dado os seus valores de entrada
    list,int,int->str"""
    
    if H>=medidas[1] and H>=medidas[2]:
        return True
    else:
        return False