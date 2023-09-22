# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que retorna uma string s com o elemento da posicao i substituido por x'''
    subs1=s[0:(i-1)]
    subs2=s[(i+1):]
    return str(subs1)+str(x)+str(subs2)