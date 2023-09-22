# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que retorna uma string s com o elemento da posicao i substituido por x'''
    a=i+1
    b=i-1
    subs1=s[0:i]
    subs2=s[a:]
    return str(subs1)+str(x)+str(subs2)