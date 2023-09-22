# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' no parametro s e x colocar uma string e em i colocamos um inteiro   '''
    if 0<=i<len(s):
        return s[:i] +x + s[(i+1):]