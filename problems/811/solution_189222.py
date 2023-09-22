# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    """função que recebe a medida de um colchão em centimetros e retorna se ele passa ou não pela porta de largura L e altura H
	list, int, int -> bool"""
    
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    
    if b <= H:
        return True
    
    else:
        return False