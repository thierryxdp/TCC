def lingua_p(mensagem):
    traducao = mensagem.lower()
    aux = 0

    for letra in mensagem: 
        if (letra in 'aeiouAEIOU'):
            vogal = letra.lower() 
            i = traducao.find(vogal, mensagem.index(letra, aux)) 
            traducao = traducao[:i] + vogal + 'p' + traducao[i:]
            aux = mensagem.index(letra, aux)

    return traducao