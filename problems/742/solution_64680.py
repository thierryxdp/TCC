# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    	Função recebe uma string(s), um caractere(x)
        e um número inteiro(i) entre 0 e o comprimento de s
        e retorna uma string igual a s, mas com x substituindo
        o elemento da posição i
        string, int, int -> string
        
    '''
    return s[:i]+str(x)+s[i:]