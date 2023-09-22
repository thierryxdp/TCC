# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Função que substitui uma letra da palavra 
    inserida no parametro s pelo parametro em x e 
    depende do parametro i
    str,int,int->str '''
    J=int(i+1)
    return s[0:i]+ x + s[J:]