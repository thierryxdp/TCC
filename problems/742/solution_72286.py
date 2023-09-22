# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que, ao receber uma string (s), troca a 
    letra da posição escolhida (i) pela letra escolhida (x)'''
    return s[:i]+x+s[i+1]