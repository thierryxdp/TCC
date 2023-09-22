#Start your python function here
def colisao(ret1,ret2):
    """funcao que identifica colisao entre dois retangulos dados suas coodenadas em
    forma tuplas .Entrada-->tupla-tupla,saida boleano"""
    n1=int(ret1[1])
    n2=int(ret1[2])
    n3=int(ret1[3])
    n4=int(ret1[4])
    p1=int(ret2[1])
    p2=int(ret2[2])
    p3=int(ret2[3])
    p4=int(ret2[4])
    if n1<p1 and n2<p2 and n3<p3 and n4<p4:
        return False
    else:
        True