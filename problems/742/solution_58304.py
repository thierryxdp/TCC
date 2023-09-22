# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Para retornar uma str igual a s, exceto o elemento da posição i que
    deve ser substituido por x, digite
    str,str,int-> str"""
    s = list(s)
    s[i] = x
    return ''.join(i)