# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string substituindo o caractere da indexação"""
    s=str(s)
    str(s)[i]=x
    return str(s)