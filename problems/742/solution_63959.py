# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string na qual o elemento da
    posicao i é substituído por x;
    string,string,int -> string'''
    return s[0:i] + str(x) + s[i+1:-1]