def busca(m, setor):
    encontra = []
    for i in range(len(m)):
        if str(setor) in m[i]:
                encontra.extend(m[i])
                
                    
    return encontra