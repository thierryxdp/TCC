# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dada a palavra s, o caractere x e a posição i que se deseja substituir x
    na palavra s, retorna a palavra com o caractere substituido na posição indicada;
    obs.: A posição do primeiro caractere na palavra s é considerada como posição 0;
    str,str,int->str'''
    if i >= len (s):
        return 'Coloque um número inteiro em i que seja entre 0 e a mesma quantidade de caractere de s'
    else:
        return s[:i] + str(x) + s[i+1:]