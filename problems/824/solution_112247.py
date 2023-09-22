def verifica_letra(letra):
    return letra if letra in 'aeiouáéíóúàèìòùâêîôûãõ' else letra.upper()
def uppCons(frase):
    return ''.join(list(map(verifica_letra, list(frase))))