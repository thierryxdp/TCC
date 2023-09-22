def busca(n,matriz):
    """
    Função que dado um nome e uma matriz, retorna os dados do nome dado.'
    Entrada:
            n - nome
            matriz dada como lista
    Saida:
           lista com os dados 
    """
    lista = []
    numero = 0
    
    for numero in range(len(matriz)):
        if n in matriz[numero]:
            lista.append(matriz[numero])
            
    for numero in range(len(lista)):
        lista[numero]=lista[numero][:1]+lista[numero][3:]
        
    return lista