def lingua_p(palavra):
    '''Funçao, dada uma palavra em português, retorna sua composição
    traduzida para a 'lingua do P'
    string -> string''' 
    palavra_nova = str()
    
    for letra in palavra:
        if letra in 'aeiouéúàáíó':
            palavra_nova += str.lower(letra)+'p'+str.lower(letra)
        if letra not in 'aeiouéúàáíó':
            palavra_nova += str.lower(letra)
            
    return palavra_nova