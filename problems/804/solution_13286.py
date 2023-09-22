# Função que retorna a filtragem de uma tupla de 4 elementos, apenas com seus elementos pares
#  int,int,int,int -> tuple
def filtra_pares(p1,p2,p3,p4):
    tupla_filtrada = ()
    if  p1%2==0:
        tupla_filtrada = tupla_filtrada + (p1,)
    if p2%2==0:
        tupla_filtrada = tupla_filtrada + (p2,)
    if p3%2==0:
        tupla_filtrada = tupla_filtrada + (p3,)
    if p4%2==0:
        tupla_filtrada = tupla_filtrada + (p4,)
    return tupla_filtrada