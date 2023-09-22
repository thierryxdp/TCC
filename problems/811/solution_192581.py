def  colchao ( medidas , H , L ):
    """
    Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e L.
    :param medidas: list -> list
    :param H: int -> int
    :param L: int -> int
    :return: bool -> bool
    """
    [ A , B , C ] =  medidas
    se  A  e  B  >  H  e  L :
        return  Falso