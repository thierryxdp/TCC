def lingua_p(palavra):
    """Calcula e retorna a traducao da variavel de entrada "palavra"
    escrita em portugues para a lingua P;str-->str"""
    traducao=""
    for i in range(len(palavra)):
        if palavra[i] in "AaEeIiOoUu":
            mudanca=palavra[i]+"p"+palavra[i]
            traducao=traducao+str.replace(palavras,palavra[i],mudanca)
    return str.lower(traducao)