# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Função retorna uma string igual a s,exceto que o elemento da
    prosição i deve ser substituído pelo caractere x.'''
    return s[0:i]+x+s[i+1:len(s)]