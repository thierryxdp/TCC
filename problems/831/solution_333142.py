def lingua_p(palavra):
    """Calcula e retorna a traducao da variavel de entrada "palavra"
    escrita em portugues para a lingua P;str-->str"""
    traducao=""
    for i in range(len(palavra)):
        if str.lower(palavra[i]) == "aãeéêiíuo":
            traducao=traducao+str.replace(palavra,palavra[i],palavra[i]+p+palavra[i])
    return str.lower(traducao)