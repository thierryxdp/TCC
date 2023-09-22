# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao retorna as variaveis de substituicao com caractere
    str,str,int-> string
    '''
    a= s[0:i]
    b= s[i+1:len(s)]
    
    return a + x + b