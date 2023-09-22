def lingua_p (palavra):
    palavra=str.lower(palavra)
    nova=palavra
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in range(len(palavra)):
        if palavra[i] in vogal:
            nova=nova.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
    return nova