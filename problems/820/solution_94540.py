def posLetra(s,l,n):
    """
    Função que recebe uma string 's', uma letra 'l' e um número 'n'
    e retorna o indice da aparição de número n da letra l na string s.
    Se não houverem n aparições da letra l, a função retornará -1.
    
    str, str, int ---> int
    """
    
    ocorrencia=0
    index=-1

    if s.count(l)<n:
        return -1
    while ocorrencia != n: 
        index = s.index(l,index+1)
        ocorrencia+=1
    return index