# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """."""
    s = str(s)
    lista = [s,x,i]
    return lista[:1] + x + lista[i+1:]