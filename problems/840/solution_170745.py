def bolos(x,o,l):
    """Calcula quantos bolos joão fara com a quantidade de ingredientes que ele tem;
    int,int,int ==> int or str"""
    trigo= int( x/2)
    ovos = int( o/3)
    col_leite= int(l/5)
    ingredientes = [trigo,ovos,col_leite]
    if trigo == ovos and ovos==col_leite:
        return trigo
    elif trigo>0 and ovos >0 and col_leite>0:
        menor=min(ingredientes)
        return menor