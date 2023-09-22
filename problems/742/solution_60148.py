# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funçao que retorna uma string igual a s, exceto que o elemento da posiçao i 
    deve ser substituido pelo caractere x"""
    a = str(s[:i])
    b = str(s[i+1:])
    return str(a)+ str(x)+ str(b)