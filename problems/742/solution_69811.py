# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    word= s
    lst=[]
   
    
    for i in word:
        lst.append(i)
    letra= lst[i]
    s.replace(letra,x)
    return s