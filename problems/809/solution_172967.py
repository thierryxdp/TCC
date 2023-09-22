# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Gera uma nova lista a partir da junção de duas listas dadas, contendo
       3 elementos cada,intercalando seus elementos;
       tuple,tuple->tuple
       Parametros:
       lista1: 1°lista com 3 elementos
       lista2: 2°lista com 3 elementos
    """
    
    a,b,c=lista1
    d,e,f=lista2
    
    return [a,d,b,e,c,f]