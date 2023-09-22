# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Funcao que retorna a string posta so que com o X na posicao I da string. str,str,int -> str"
    if  i > len(s) - 1:
        return "Dados inválidos"
    elif i == 0:
        return x + s[1:]
    else:
        return s[0:i] + x + s[i+1:]