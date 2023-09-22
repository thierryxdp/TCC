# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''A função recebe uma string (s) e substitui por caractere (x) na posição que o usuário escolhher (i) '''
    return s[0:i] + str(x) + s[i+1:]