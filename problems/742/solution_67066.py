# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
       função que em s,x,i recebe respectivamente uma string, um caractere e um inteiro 
       de acordo com o tamnho da str. Retorna uma str semelhante à recebida, 
       substituindo o caractere x.
       str,str,int --> str
    '''
    s = s[:i] + x + s[i+1:]
    return s