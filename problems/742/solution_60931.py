# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''calcula e retorna uma string igual a s, exceto que
    o elemento da posicao i deve ser substituido pelo caractere x;
    int, int->str'''
    return s[0:i]+x+s[i+1:]