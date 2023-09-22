# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que, dada uma string s, um caractere x e um número
    inteiro i entre 0 e o comprimento da string, retorna uma string
    igual a s, tal que o elemento em i é substituido por x'''
    return str(s)[0:i]+str(x)+str(s)[i+1:len(str(s))]