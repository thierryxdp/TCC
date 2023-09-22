"""recebe uma string, retorna (na primeira função) os elementos separados por espaços em uma lista e retorna o inteiro equivalente a contagem desses elementos
Assinatura str-> int"""
def separa(f):
    return f.split()
def quant_palavras(f):
    return len(separa(f))