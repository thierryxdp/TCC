def posLetra(string,letra,n):
    """Função que retorna a ocorrencia de uma letra dada uma string
    str,str,int->int"""
    i=0
    ocorrencia=0
    while i<len(string):
        if string[i] == letra:
            occorencia +=1
            if ocorrencia == n:
                return i
        i +=1
        if occorencia<n:
            return -1