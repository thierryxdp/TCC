def verifica_letra(letra:str)-> str:
    '''Verifica se a letra recebida é consoante ou vogal, caso seja 
    consoante retorna-a maiúscula'''
    return letra if letra in 'aeiouáéíóúàèìòùâêîôûãõ' else letra.upper()
def uppCons(frase:str)-> str:
    '''Retorna a frase com todas suas consoantes em maiúsculas'''
    return ''.join(list(map(verifica_letra, list(frase))))