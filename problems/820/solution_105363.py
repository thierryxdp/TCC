def posLetra(string,letra,numero):
    """funçãao que retorna a posição da letra(indicada no parametro de entrada),dada a string a qual ela
    se localiza,  propria letra e o numero de sua ocorrência"""
    # a função retornará -1 se caso a ocorrência informada na entrada for menor que a real ocorrÊncia
    a=0
    posicao=0
    while a<=str.index(string,letra,numero):
        if str.index(string,letra,numero)<=numero:
           posicao+=numero
    a+=posicao
        else :
               return -1
    return a