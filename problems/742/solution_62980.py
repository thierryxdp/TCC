# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'essa função substitui um caractere da posição i por x de uma string s, string,string,int->string'
    if i != 0:
        s1=s[0:i-1]
        s2=s[i-1:]
        s2=s2.replace(s2[1],x,1)
        return s1+s2
    else:
       return s.replace(s[0],x,1)