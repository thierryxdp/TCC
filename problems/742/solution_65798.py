# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Essa função recebe a string 's', um número inteiro 'i' entre 0 
    e len(s) e retorna uma string igual a s, com s[i] = x
    """
    s[i] = x
    return s