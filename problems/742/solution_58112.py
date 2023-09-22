# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função em que dada uma string s, uma caractere x e u número inteiro i entre 0 e o comprimento da string retorna uma string igual a s exceto em relação ao elemento da posição i, que é subtituído por x.
    string, string, int -> string"""
    stwing = s[0:i]
    stwong = s[i+1:]
    return stwing + str(x) + stwong