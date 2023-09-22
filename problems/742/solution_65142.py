# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que substitui um elemento de uma posição
    qualquer da string por um caracter. Recebe como
    parâmetro uma string ,de qualquer tamanho, caracter 
    e posição dada pelo usuário. 
    String, String, int---> String.'''
    return s[:i:]+x+s[i+1::]