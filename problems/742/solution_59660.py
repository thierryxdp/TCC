# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
 	string = str(s)
    y = string[0:(i)]
    z = string[(i)+1:]
    print (y+x+z)