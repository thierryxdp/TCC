#Função que receba uma string s, um caractere x e um número i entre 0 
# e o comprimento da string e retorne uma srtind igual a s.
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i < 0 or i >= len(s):
        return "erro"
    else:
        return s[:i] + x + s[i+1:]