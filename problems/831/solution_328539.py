def lingua_p(palavra):
    """A função definida recebe uma palavra (em português).
    Todas as vogais da palavra original devem ser sucedidas
    pela letra'p' mais a vogal original que antecede 'p'. 
    Ao retornar essa palavra - traduzida toda em minúsculo,
    devem ser feitas todas essas modificações.
    Entrada: String
    Saída: String"""
    
    vogais='aàáãâeéêiíoóôõuûú'
    novap=''
    
    for letra in palavra:
        if letra in vogais:
            novap +=novap+str(letra+"p"+Letra)
        else: 
            novap += letra
    return str.lower(palavra)