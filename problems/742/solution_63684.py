# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Retorna a string s com o carater x na posição i
    	str, str, int -> str
        Explicação: Separa s entre 0 e i, concatena com x e concatena com s entre 1+1 até o fim'''
    ret = s[0:i] + x + s[i+1:]
    return ret