def lingua_p(palavra):
    for letra in  ['a','e','i','o','u','b', 'c', 'ç','d', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z',]:
    
        if letra in palavra :
            palavra=letra +'p'+letra
            
            
    return (palavra)