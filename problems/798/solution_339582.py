def freq_palavras(frases):
    """ Função que recebe uma string e retorna um dicionario onde a chave de cada string sera as vezes no qual se repete. input string, return dict """

    palavras = []
    contagem = []
    resposta = {}
    
    
    palavras.append(frases.split())
    
    for i in palavras:

        x = palavras.count(i)

        contagem.append(x)

        resposta{i} = x
            
        palavras.remove(i)

    return resposta