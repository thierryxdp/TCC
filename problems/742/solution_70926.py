# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função recebe uma string s, uma integral x e um numero i e retorna a string s, substituindo o elemento na posição i por x
    """
    string0=str(s)
    string1=string0[0:i]
    string2=string0[i:]
    return str(string1)+str(x)+str(string2)