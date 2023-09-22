# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string s e retorna uma string na qual o caractere da posicao i (entre 0 e o comprimento da string) e substituido pelo caractere x; str,str,int -> str'''
    return s[0:int(i)] + x + s[int(i+1):]