# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string igual a s, exceto que o elemento da posição i é substituído pelo x.'''
    
    novo_s = s[0:i] + str(x) + s[i+1:]
    return novo_s