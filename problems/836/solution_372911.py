def busca(setor, m):
    
    resultado = []
    for funcionario in m:
        if setor in funcionario:
            funcionario.remove(setor)
            resultado.append(funcionario)
           
        
    return resultado