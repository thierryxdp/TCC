def freq_palavras(frases):
    '''
    função que retorna um dicionário atribuindo uma chave a cada palavra de uma string,
    mostrando o numero de vezes que cada palavra aparece, após a frase ser inserida na entrada. 
    str -> dict
    '''
    contagem_palavras = {}
    palavras=str.split(frases)
    
    for qtd in palavras:
        if qtd in palavras:
            contagem_palavras[qtd]=list.count(palavras,qtd)
    return contagem_palavras