def acima_da_media (notas):
    """
    Essa função define os números que estão acima da média. 
    Fazendo a soma de todos os itens, depois dividindo pela quantidade de itens,
    por último verifica quais estão com valores acima desse resultado
    
    Parametro de entrada: list
    Valor de Saída: string
    """
    q=len(notas)
    s=sum(notas)
    m=s/q
    if m in notas:
        list.remove(notas,m)
        aprovados=maiores(notas,m)
        return aprovados
    else:
        aprovados=maiores(notas,m)
        return aprovados