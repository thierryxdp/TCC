def colchao(medidas: list, H: float, L: float) -> bool:
    """Recebe uma lista com as medidas do colchão - ordenadas da menor para
    maior - a altura H e largura L da porta. Retorna se o colchão pode passar
    pela porta, com uma das suas faces virada para baixo."""
    #Presumida menor medira é a 'profundidade' - grossura - do colchão.
    prof_colchao = medidas[0]
    #Presumida segunda maior medida como largura do colcão.
    larg_colchao = medidas[1]
    #Presumida maior medida como comprimento do colchão.
    comp_colchao = medidas[2]
    #Nomes apenas elucidativos
    
    #Se o colchao passa com a face largxcomp paralela ao chão
    if prof_colchao <= L and larg_colchao <= H:
        return True
    #Se o colchão passa com a maior face (compxlarg) paralela ao chão
    elif larg_colchao <= L and prof_colchao <= H:
        return True
   	else:
        return False