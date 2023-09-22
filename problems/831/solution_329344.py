def lingua_p(palavra):
    """função que recebe uma palavra em português e a retorna 
    traduzida para a lunguagem do p: str->str"""
    resposta=''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            letra=str.lower(letra)
            resposta='p'+letra+'p'
        elif:
            resposta + letra
    return resposta