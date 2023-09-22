def lingua_p (palavra):
    palavra=str.lower(palavra)
    nova=palavra
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in list(range(len(palavra))):
        if palavra[i] in vogal:
            if str.count(palavra,palavra[i])==1:
                nova=nova.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
            else:
                nova=nova.replace(palavra[i+2],(palavra[i+2]+'p'+palavra[i+2]))
    return nova