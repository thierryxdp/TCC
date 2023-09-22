# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' recebe uma string s, um caractere x, e um número inteiro i, entre
    zero e o comprimento da string e retorna uma string igual a s, exceto
    que o elemento da posicao i, deve ser substituido pelo caracter x '''
    tamanhoString = len(s)
    s[0:tamanhoString]
    fatia1 = s[0:i]
    fatia2 = s[i:]
    resultado = str(s[0:i] + str(x) + s[(i+1):])
    return resultado