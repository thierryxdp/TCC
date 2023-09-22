# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    #i=int(i)
    #s= str(s)
    #x= str(x)
    #new= len(s)
    #new = s[len(s)i]
    new_str= s[i]
    resp= s.replace(new_str,x)
    return resp