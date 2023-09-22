# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Essa funçao pega uma string s e troca o elemento de numero i por x.
    str -> str'''
    if i>= 0 and i<- len(s):
        nova_s = s[0 : i] + 'x' + s[i+1 :]