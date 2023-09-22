def posLetra(string,letra,ocorrencia):
    """funçãao que retorna a posição da letra(indicada no parametro de entrada),dada a string a qual ela
    se localiza,  propria letra e o numero de sua ocorrência"""
    # a função retornará -1 se caso a ocorrência informada na entrada for menor que a real ocorrência
    a=0
    p=0 #posição
    if letra not in string or ocorrencia > str.count(string,letra):
        return -1 
    else:
        while ocorrencia!=0:
               p=str.find(string,letra,a)
               a= p+1
               ocorrencia-=1
    return p