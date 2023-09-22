# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i<0 or i>=len(s):
        return 'o valor i deve estar entre 0 e o omprimento da strings'
    else:
        return s[0:i]+str(x)+s[1+i:]