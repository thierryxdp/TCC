def Trigo(trigo):
    '''Dado o número de xícaras de farinha de trigo, 
    retorna a quantidade exata de xícaras que podem ser 
    usadas na receita.
    int -> int'''
    return trigo//2

def Ovos(ovos):
    '''Dado o número de ovos, retorna a quantidade exata 
    de ovos que podem ser usadas na receita.
    int -> int'''
    return ovos//3

def Leite(leite):
    '''Dado o número de colheres de sopa de leite, retorna
    a quantidade exata de colheres que podem ser usadas na
    receita.
    int -> int'''
    return leite//5

def bolos(trigo, ovos, leite):
    '''Dados o número de xícaras de farinha de trigo, o
    número de ovos e o número de colheres de sopa de leite,
    retorna a quantidade máxima de bolos que João consegue
    fazer.
    int,int,int -> int'''
    return min(Trigo(trigo),Ovos(ovos),Leite(leite))