# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''A substituição de um elemento de uma string por outro, (s=string),
(x=elemento),(i=número),exemeplo: pedro=s,P=x,0=i ->Pedro, (str,str ou int,int->str)'''
     s= s[0:i]+str(x)+s[(i+1):len(s)]
     return s