def posLetra(frase,letra,ocorrencia):
    """Função que retorna a posição da string em que a ocorrencia 
    desejada da letra está, dados 'frase' 'letra' e 'ocorrencia',
    caso exista menos ocorrencias da letra do que a ocorrencia pedida
    a função retornará -1
    str, str, int -> int"""
    posicao=0
    if ocorrencia > str.count(frase,letra):
        return -1
    while ocorrencia>0:
        posicao= str.find(frase,letra,posicao)
        posicao=posicao+1
        ocorrencia=ocorrencia-1
        
    return posicao1