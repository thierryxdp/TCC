# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Informa se o colchão com medidas definidas pela 
    lista medidas pode passar pela porta definida por H e L.
    list, int, int -> bool"""
    a = medidas[1]
    if a <= H:
        return True
    else:
        return False