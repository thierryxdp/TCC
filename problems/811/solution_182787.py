# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Dado como entrada umas lista com as dimensões de um colchão, 
    contendo espessura, largura e altura, expressos em ordem crescente, 
    e as dimensões de uma porta, sendo H a altura e L a largura, retorna
    o booleano True, se o colchão passar pela porta, ou False, caso 
    contrário;
    lista(float,float,float),float,float->booleano"""
    md=medidas
    if md[0]<=L and md[1]<=H or md[2]<=H and md[0]<=L or md[1]<=L and md[2]<=H:
        return True
    else:
        return False