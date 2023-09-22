# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que, dado um string s, um caractere x e um número inteiro i, retorna a string s sem o elemento
    de ordem i, substituindo-o por x'''
    s = str(s)
    x = str(x)
    if i>0:
        nova_string = s[0:i]+x+s[(i+1):]
        return nova_string
    elif i==0:
        nova_string = x+s[1:]
        return nova_string
    else:
        nova_string = s[-1:i]+x+s[(i-1):]