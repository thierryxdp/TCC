def busca(s,m):
    """Função que recebe uma string para busca e uma matriz m e retorna as informações dos funcionários. String, List-> List"""
    l=[]
    res=[]
   
    for j in range (len(m)):
            if m[j][2] == s:
                res=res+[[m[j][0],m[j][1],m[j][3]]]
    return res