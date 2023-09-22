# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    tam=len(s) #define o tamanho da palavra
    qttd=s.count(s[i]) #conta a quantidade de letras iguais àquela na posição i
    if qttd>1:
        return str.replace(s,s[i],x,2)
    else:
       	return str.replace(s,s[i],x,1)