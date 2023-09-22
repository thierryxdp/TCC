# verifica se esse colchão passa pela porta de altura H e largura L
# Medidas , H , G 
def  colchao ( Medidas , H , G ):
    """Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e largura L.
    : param medidas: lista -> lista
    : param H: int -> int
    : param L: int -> int
    : return: bool -> bool"""
    [ A , B , C ] =  Medidas
    se  A  e  B  >  H  e  L :
        retornar  falso
    mais :
        retornar  verdadeiro
imprimir ( colchao ([ 25 , 200 , 220 ], 200 , 100 ))