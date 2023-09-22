def lingua_p(palavra):
    frase=0
    vogais='aeiouAEIOU'
    
    for vogais in palavra:
         if vogais in palavra:
            frase='p'.join(vogais) 
            frase=frase+vogais
            
        

    return frase