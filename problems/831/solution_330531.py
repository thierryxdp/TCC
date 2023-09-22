def lingua_p (palavra):
    palavra=str.lower(palavra)
    nova=palavra
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in range(len(palavra)):
        #banana = [0,1,2,3,4,5]
        if nova[i] in vogal:
            nova=palavra.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
    return nova