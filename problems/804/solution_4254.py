def filtra_pares([a,b,c,d]):
    """Função que dada uma tupla com 4 elementos inteiros retorna uma nova 
       tupla contendo apenas os elementos pares da tupla original, na mesma
       ordem que se encontravam.
       tupla->tupla
       
       Parâmetros:
       [a,b,c,d]:É uma tupla com quatro elementos inteiros que serão
                 avaliados pela função.
       
       returns:Uma nova tupla contendo apenas os elementos pares da tupla original, na mesma
       ordem que se encontravam.
    """
    tupla1 = [a,b,c,d]
    return list(filter(lambda x: x%2==0, tupla1))