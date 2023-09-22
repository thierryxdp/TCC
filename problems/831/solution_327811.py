def lingua_p(palavra):
    '''Função, dada uma palavra em português, retorna sua composição
    traduzida pra língua do P'''
    palavra_nova = str()
    
    for letra in palavra:
        if letra in 'aeiouéúáàíó':
            palavra_nova+= str(letra)+'p'+str(letra)
        if letra not in 'aeiouéúáàíó':
            palavra_nova+=str(letra)
           
    
    return palavra_nova