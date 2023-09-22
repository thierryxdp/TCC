# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    dado a string s, caracter x e um numero inteiro i
    retorna uma string s no entanto o caracter x estará substituindo
    o caracter da posição i da string s
    entrada:str,str,int
    saida:str
    '''
    
    return s[0:i]+x+s[(i+1):(len(s))]