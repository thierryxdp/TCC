# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Retorne uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x
        
        Parameters:
            s = string inserida a ser alterada (deve ser digitada entre aspas)
            x = caractere a ser inserido na string (deve ser digitada entre aspas)
            i = número inteiro entre 0 e o comprimento da string
        
        Testes:
            substitui("oio","o",1) = "ooo"
            substitui("tudo bem?","!",8) = "tudo bem!"

        Returns:
            Uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x
            str, str, int -> str.
    """
    primeira_parte = s[:i]
    segunda_parte = s[i+1:]
    
    return primeira_parte+x+segunda_parte