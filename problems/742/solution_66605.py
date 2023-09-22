"função que retorna uma string dados uma string qualquer,com caracter quaquer e um número inteiro que vale de 0 ao valor máximo da string inicial"
"str,int,str->str"

def substitui(s,x,i):
    a=i+1
    b=len(s)
    strinicial=s[0:i]
    strfinal=s[a:b]
    return strinicial + str(x) + strfinal