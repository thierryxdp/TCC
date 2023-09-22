def par(x):
    """Função que dado um número x retorna ele próprio caso seja par e "" 
       caso seja ímpar.
       int->int
       
       Parâmetros:
       x: Número que será verificado se é par.
       
       returns:O próprio número caso seja par e "" caso seja ímpar.
    """
    if (x%2)==0:
        return x
    else:
        return ""

def filtra_pares ([a,b,c,d]):
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
    [a,b,c,d] = tupla1
    return tuple(filter(lambda x: par(x), tupla1)