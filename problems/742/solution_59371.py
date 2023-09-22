def substitui(s,x,i):
    """Funcao que recebe uam string s, um caractere x e um numero 
    inteiro i, retornando uma string igual a s e substituindo i por x"""
i = len(s)-1
if i >0:
    return s(:i)+x+s(i+1:)
else:
    return 'Insira um inteiro válido'