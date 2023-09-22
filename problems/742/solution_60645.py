# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    """Função que retorna a string s da entrada, substituindo o
    seu caractere de índice i por um caractere x"""
    
    return s[0:i] + str(x) + s[i+1:len(s)]