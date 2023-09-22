# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    # retorna uma string que seja igual a s, tendo o elemento na posição i sendo substituido por x.
    s[i]=x
    return s[0:i] + x + s[i+1:]