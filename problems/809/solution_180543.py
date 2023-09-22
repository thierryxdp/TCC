def intercala(list_no1, list_no2):
    """
    Funçao que gera uma 3a lista com elementos intercalados de 2 outras listas
    de tamanho 3 cada.
    list_no1 -> elementos lista 1
    list_no2 -> elementos lista 2

    (list[str,str,str], list[int,int,int]) -> list[str,str,str,str,str,str]
    """
    return [list_no1[0],list_no2[0],list_no1[1],list_no2[1],list_no1[2],list_no2[2]