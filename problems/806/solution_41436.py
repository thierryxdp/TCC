#Start your python function here
def colisao(ret1,ret2):
"""funcao que identifica colisao entre dois retangulos dados suas coodenadas em
    forma tuplas .Entrada-->tupla-tupla,saida boleano"""
    if ret1[3]<ret2[2]:
        return False
    else:
        return True