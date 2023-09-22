def substitui(s,x,i):
    """Muda a letra da posição escolhida para o caractere fornecido"""
    return str(s[0:i])+str(x)+str(s[(1+i):len(s)])