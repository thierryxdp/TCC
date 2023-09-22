def substitui(s,x,i):
    """recebe uma string s, um caractere x e uma posição i, retira o caractere da posição i e insere o x; str + str + int --> str"""
    var1 = s
    var2 = var1[0:i] + x
    var3 = var1[1+i:]
    return var2 + var3