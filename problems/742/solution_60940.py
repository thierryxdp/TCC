# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe duas strings e um números inteiros 
    	e substitue um caractere s[i] da string 
        s pelo caractere x
        str, str, int -> str"""
    caractere = str(x)
    return s[0:i] + caractere + s[i+1:]