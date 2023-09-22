# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string igual a s, substituindo a posição i pelo caractere x.
       str, str, int -> str."""
    return str (s)[0:i] + x + str (s)[i+1:]