# FUnção que substitui uma string s cortanto a string até i e somando x e adicionando a sobra a partir de i+1 até o 
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    termos_palavra= len(s)
    corte=s[0:i]
    sobra=s[i+1:termos_palavra]
    return corte+x+sobra