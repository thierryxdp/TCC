def substitui(s,x,i):
    """Funcao que recebe uma string, um caractere e retorna uma string com o caractere
    na posicao fornecida(i);
    str, str, int - str"""
    pos1 = str(s[:])
    pos2 = str(x)
    pos3 = int(i)
    pos4 = int(pos3+1)
    return pos1[:pos3]+pos2+pos1[pos4:]