# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    	Função que retorna uma string semelhante à string s,
        porém com o elemento da posição i substituído
        pelo caractere x, sendo que i é um número inteiro
        entre 0 e o comprimento da string s
        : param s: str
        : param x: int
        : param i: int
        : return: str
    '''
    posicao_depois_i = i + 1
    return s[:i] + str(x) + s[posicao_depois_i:]