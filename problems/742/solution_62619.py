funcao que substitui "x", "s" e "i" que recebe uma string "s" um caractere "x" e um numero inteiro "i" entre 0 e o compriemnto da string e retorna uma string igual a "s"  execeto que o elemento "i" deve ser subtituido pelo caractere "x" 
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    a=len(s)
    corte=s[0:i]
    sobra=s[i+1:a]
    return corte+x+sobra