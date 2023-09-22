# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' função que substitui uma str, str e um numero int, e retorna uma str igual a s, exceto que o elemento da posição i deva ser substituido pelo caractere x
    '''
    if i >= len(x) or 0 <= i:
         return s[:1] + str(x) + s[i+1]
    else:
         return 'não é possivel fazer a substituição'