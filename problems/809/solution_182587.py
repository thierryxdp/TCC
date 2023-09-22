def siga(t):
    """recebe uma tupla com um nome e tres notas e retorna o nome a media e a situação do aluno
    tuple(str,int,int,int) -> tuple(str,int,str)"""
    a,b,c,d = t 
    if (b+c+d)/3 >= 7:
        return ((a  , (int((b+c+d)/3)) ,  "aprovado , parabéns!"))
    elif 5 <= (b+c+d)/3 < 7:
        return ((a , (int((b+c+d)/3)) , "aprovado"))
    else:
        return ((a , (int((b+c+d)/3)) , "reprovado"))