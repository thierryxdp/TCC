def lingua_p(palavra):
    i=0
    resultado=''
    
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            palavra+= letra+'p'+letra
        else:
            resultado+=letra
            
        resultado += palavra.lower()
        i+=1
        
    return resultado