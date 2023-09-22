def bolos(a,b,c):
    """Calcule e retorne a quantidade máxima de bolos que se pode fazer"""
    a1=a/2
    b2=b/3
    c3=c/5
    minimobolos=min(a1,b2,c3)
    minimointeirobolos=int(minimobolos)
    return minimointeirobolos