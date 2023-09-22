# Essa função serve para substituir um caracter específico na string
# string, int, int -> string
def substitui(s,x,i):
    p1 = s[0:i]
    "a p1 recebe a parte do início à antes do caracter desejado"
    p2 = s[i+1:]
    "a p1 recebe a parte após o caracter desejado até o final"
    return p1 + x + p2
	"soma estas duas partes colocando o caracter x entre eles, causando a substituição"
    
#casos de teste:
"""
substitui("lixo", "a",3) == lixa


"""