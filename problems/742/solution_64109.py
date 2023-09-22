# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma str igual a str de entrada str s, com a 
    diferença que a posição i é substituída pelo elemento x
    valor de entrada: str s, str x e int i 0<i<len(str s)
    valor de saída: str'''
    return s[0:i]+str(x)+s[i+1:]