# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
#Subistituicao
def substitui(s ,x , i):
    """Recebe uma string, uma posção na string e um caractere e substitui esse caractere em determinada posição na string
    str + int + str -> str"""
    a = list(s)
    a[i] = x
    return str.join("",a)