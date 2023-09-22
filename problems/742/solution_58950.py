# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorna uma string igual a s, exceto que o elemento
    da posição i deve ser substituído pelo carctere x'''
    a=i+1
    return s[0:i]+str(x)+s[a:]