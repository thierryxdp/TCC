# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i): 
    if 0<=i<len(s):#conta quantos elementos tem dentro da string
        return (s[:i]) + x +(s[(i+1):])#retorna o inicio da string até o