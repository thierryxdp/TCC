#Essa função já é um pouco mais complexa
#Nela utilizei tres parametros (s, x, i)
#Esses parametros são entradas para string, numero inteiro e caractere
def substitui(s,x,i):
    """
    recebe s: string
	recebe x: caractere
    recebe i: int
    """
    return s[0:i] + x + s[i + 1:]
#Feita a função ela recebe a str s, o caractere, o int entre 0 e o comprimento da string
#Me retorna a str igal a s, menos pelo fato da posição i ser subistituida por x