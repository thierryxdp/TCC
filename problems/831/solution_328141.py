def lingua_p(palavra):
    s=[palavra]
    for letra in palavra :
        if letra in ['a','e','i','o','u']:
            palavra=s.pop(letra +'p'+letra)
            
            
    return (palavra)