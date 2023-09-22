# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    	Essa função recebe uma string s, um caracter x e
        um número inteiro i entre 0 e o comprimda da string,
        e retorna ua string igual a s excdeto que o elemento 
        da posição i é substiruído por x.
    '''
    return s[:i] + x + s[i+1:]