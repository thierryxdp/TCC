"""A função ira pegar 'x' que é um string e ira renomear  "...""." "?" "!" 
e ira renomeala como "/" , usando a função split ela ira remover "/" e separar
a string, usando "len" que ira contar o numero de elementos e também descontando menos 1 da caixa vazia
que fica no final de cada frase, a função ira retornar o numero de frases.

str --> Int"""

def conta_frases(x):
    A = x.replace("...","/")
	B = A.replace(".","/")
    C = B.replace("?","/")
    D = C.replace("!","/")
    E = D.split("/")
    return len(E)-1