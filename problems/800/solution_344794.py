def total (produto,preco):
    """."""

    resposta = 0

    for i in produto:
        if produto in preco:
            resposta = resposta+preco[i]

            
    return round(resposta,2)