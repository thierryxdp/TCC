def faltante(lista):
    """Dada uma lista com N-1 numeros inteiros, retorna o número inteiro 
       que está faltando na lista no intervalo de N-1;
       list->int
       Parametro:
       lista: lista de tamanho N-1 de numeros inteiros
    """
    i=0
    list.sort(lista)
    pecafaltante=list(range(1,(len(lista)+2)))
    if lista[len(lista)-1]!=pecafaltante[len(pecafaltante)-1]:
        return pecafaltante[len(pecafaltante)-1]
    else:
        while lista[i]==pecafaltante[i]:
            i=i+1
        return pecafaltante[i]