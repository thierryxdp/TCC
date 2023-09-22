# Coloque um comentário dizendo o que a função faz
def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um número inteiro i
    	entre 0 e o comprimento da string e retorna uma string s com o elemento
        da posição i substituído pelo caractere x.
        str,str,int -> str
        """
    return s[0:i]+str(x)+s[i+1:]