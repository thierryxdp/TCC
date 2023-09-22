def posLetra(texto,letra,ocorrencia):
    """funcao que retorna a posicao de uma letra em um texto dada a ocorrencia;
    str,str,int"""

    i = 0
    texto = list(texto)
    parte = []
    qtd = texto.count(letra)
    
    if  qtd < ocorrencia:
        return -1
   
    
    while i< len(texto):

        if texto[i] == letra:
            list.append(parte,i)

        i = i + 1

    return parte[(ocorrencia - 1)]