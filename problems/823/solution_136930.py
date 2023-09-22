def faltante(lista):
    """Função que, dada uma lista com N-1 inteiros numerados
    de 1 a N, retorna qual o número inteiro do intervalo está
    faltando.
   	lista->int"""
    i=0
    while i < len(lista):
        lista.sort()
        if i+1 != lista[i]:
            return i+1 #retorna quando lista[i] não corresponde ao valor que seria i+1
        i=i+1
    return len(lista)+1 #Percorreu todos, então só pode ser o último