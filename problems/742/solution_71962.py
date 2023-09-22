# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    #str, int, int > str
    if i > len(s):
      print('i inválido')
    else:
        return s[0:i] + str(x) + s[i + 1:]