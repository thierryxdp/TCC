def retira_pontuacao(frase, palavra, pos):
    """DOCUMENTAÇÃO"""
    lista_das_palavras = str.split(frase)
    if palavra in lista_das_palavras:
        #transformar a palavra em maiúsculas e retornar a frase modificada
        pos_ocorrencia = list.index(lista_das_palavras,palavra)
        lista_das_palavras[pos_ocorrencia] = str.upper(palavra)
        return str.join(' ',lista_das_palavras)
    else:
        #adicionar a palavra como a i-ésima palavra da frase, retornando a frase nova
        list.insert(lista_das_palavras,pos,palavra)
        return str.join(' ',lista_das_palavras)