# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    sub1=s[0:i]
    sub1[i]=x
    sub2=s[i+1:len(s)]
   
    
    
    return sub1+sub2