def media_matriz(matriz):
    """dada uma matriz, retorna a media de todos os numeros da matriz"""
	quantidade=[]
    adicao=[]
    quantidade_matriz=len(matriz)
    for numeros in range(quantidade_matriz):
        quantidade_elem=len(matriz[numeros])
        A=sum(matriz[numeros])
        list.append(quantidade,quantidade_elem)
        list.append(adicao,A)
        adicao2=(sum(adicao))
        quantidade_total=(sum(quantidade))
    return (round((adicao2/quantidade_total),2))