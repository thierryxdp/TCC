def lingua_p(palavra):
    """Calcula e retorna a traducao da variavel de entrada "palavra"
    escrita em portugues para a lingua P;str-->str"""
    traducao=palavra
    for i in range(len(palavra)):
        if str.lower(palavra[i]) in "aãeéêiíuo" and palavra[i-1] != "p":
            traducao= str.replace(traducao,palavra[i],palavra[i]+"p"+palavra[i])
    return str.lower(traducao)