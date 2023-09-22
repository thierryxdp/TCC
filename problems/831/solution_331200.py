def lingua_p (palavra):
    palavra=str.lower(palavra)
    nova=palavra
    vogal='aeiouáéíóúãõãêîôûàèìòù'
    for i in vogal:
        if i in palavra:
            nova=nova.replace(i,(i+'p'+i))
    return nova