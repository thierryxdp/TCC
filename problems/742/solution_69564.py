# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' '''
    palavra= str(s)
    num= i>= 0 or i <= len(palavra)
    return palavra.replace(x,palavra[num])