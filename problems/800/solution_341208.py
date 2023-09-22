def total (produtos,dicionario):
    soma = 0 
    for corredor in range (len (produtos)):
        if produtos [corredor] in list (dict.keys(dicionario)):
            soma = soma + dict.get (dicionario, produtos [corredor])
            
    return round (soma,2)