# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Essa função, dada uma string s, um caractere x e
	 um número inteiro i entre 0 e o comprimento da string s,
	 retorna uma string igual a a, exceto que o elemento da posição i
	 deve ser substítuido pelo caractere x.
     str, str, int -> str"""
    
    #Dividindo a string em duas partes e concatenando-as com o elemento x ocupando a posição i
    string_final = s[:i] + x + s[i+1:]
    return string_final