# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado um texto ou palavra s, um caractere x e um número inteiro i, retorna
    a o texto ou palavra s com o caractere na posição i, substituído por x:
    str,str,int-->str"""
    len_s=len(s)
    return s[0:i]+x+s[i+1:len_s]