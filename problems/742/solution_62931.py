# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que com a string (s), um caractere (x) e um número
       inteiro (i) entre 0 e o valor comprimento da string, retorna
       uma string igual a s com exceção do elemento da posiçao i
       que será substituido por x.
       str,str,int->str."""
    return s[0:i] + str(x) + s[i+1:]