# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string, um caractere(x) e um numero inteiro(i), e retorna uma string igual substituindo o numero(i) 
	pelo caractere x
    str, str, int -> str"""
    
    string = s[0:i] + str(x) + s[i+1:]
    
    return string