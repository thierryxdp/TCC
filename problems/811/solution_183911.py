# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Dado como entrada a lista medidas, altura H e a largura L, retorna se o colchao consegue passar pela porta
    list,float,float==>bool"""
    hipot = (H**2+L**2)**(1/2)
    if hipot<=int(medidas[0]) or hipot<=int(medidas[1]) or hipot<=int(medidas[2]):
        return False
    else:
        return True