def lingua_p (palavra):
    palavra=str.lower(palavra)
    nova=palavra
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in range(len(palavra)):
        #banana = [0,1,2,3,4,5]
        #palavra[1]=a -> nova = bapanana
        #palavra[3]=a -> nova = bapapanana
        #palavra[5]=a -> nova = bapapapanana       
         
        #CERTO
        #palavra[1]=a -> nova[1]=a
        #palavra[3]=a -> nova[5]=a
        #palavra[5]=a -> nova[7]=a
        if palavra[i] in vogal:
            nova=palavra.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
    return nova