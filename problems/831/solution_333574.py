def lingua_p(mensagem): 
    traducao = mensagem.lower()
    
    for letra in mensagem:
        if letra in 'aeiouAEIOU': 
            letra = letra.lower()
            i = traducao.find(letra, mensagem.index(letra))
            traducao = traducao[:i] + letra + 'p' + traducao[i:]
            
    return traducao