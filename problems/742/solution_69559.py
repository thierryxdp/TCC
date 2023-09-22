# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' '''
    palavra= str(s)
    comprimento= len(palavra)
    num= i>= 0 and i <= comprimento
    return palavra.replace(x,palavra[i])