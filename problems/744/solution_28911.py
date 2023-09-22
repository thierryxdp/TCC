def hashtag(s):
    """funcao que recebe uma string e a retorna modificada com o carcatere # no inicio, no meio e no final dela;
       str-> str"""
    metade= len(s)//2
        return "#"+ s[0:(metade)-1]+"#"+s[metade:]