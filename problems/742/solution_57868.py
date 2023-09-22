# funcao que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s com o elemento da posicao i dubstituido pelo caractere x
# Escolha nomes elucidativos para suas variáveis
# str, str, int -> str
def substitui(s,x,i):
    a= i-1
    parte1 = s[0:a]
    b = a+1
    parte2 = s[b:]
    return parte1+x+parte2