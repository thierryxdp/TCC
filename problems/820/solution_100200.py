def posLetra(texto,letra,ocorrencia):
    """Dado um texto, uma letra e uma ocorrência, a função retorna 
    em que índice do texto se encontra tal ocorrência da letra desejada.
    	Caso exista menos ocorrências da letra do que a ocorrência
    pedida, a função vai retornar -1.
    	Exemplo (mariana, a, 3). A função retorna o número 6, pois a
    terceira ocorrencia da letra a, ocorre no índice 6.
    	O texto e a letra devem ser escritas entre aspas;
    	str,str,int --> int"""
     quantOcorrencia = str.count(texto,letra)
     indiceLetra = 0
     resposta = []
     if quantOcorrencia < ocorrencia:
        return -1
     while indiceLetra < len(texto):
        if texto[indiceLetra] == letra:
            resposta.append(indiceLetra)
        indiceLetra = indiceLetra + 1
     return resposta[(ocorrencia-1)]