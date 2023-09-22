# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dado uma string s, um caractere x e um número i retorna uma string igual a s exceto que o elemente de índice i é substituiduido por x; str,str,int->str'''
    	if i>=0:
            return s[:i] + x + s[(i+1):]
        else:
            return s[:i] + x + s[(i-1):]