def lingua_p(palavra):
    """Calcula e retorna a traducao da variavel de entrada "palavra"
    escrita em portugues para a lingua P;str-->str"""
    traducao= palavra
    for i in range(len(palavra)):
        if palavra[i] in "AaEeIiOoUu":
            traducao=traducao.replace(palavra[i],palavra[i]+"p"+palavra[i])
    return str.lower(traducao)