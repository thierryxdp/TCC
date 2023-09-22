def busca(string,matriz):
    'dado uma string e a matriz de registros, encontra e retorna todos os contatos referentes a essa busca'
    resposta=[]
    for contato in matriz:
        for dado in contato:
            if string == dado:
                list.append(resposta,[contato])
    return resposta