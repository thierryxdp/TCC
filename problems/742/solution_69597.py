# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' '''
    palavra= str(s)
    palavra2= str(x)
    num= i>= 0 and i <= len(palavra)
    nova= palavra.replace(palavra[i],palavra2)
    return  nova