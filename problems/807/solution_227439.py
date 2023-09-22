def conta_frases(frases):
    """Essa função retorna quantas frases existem em um texto informado
    string --> int"""
    
    frase_separada = str.split(str.replace(str.replace(str.replace(str.replace(str.strip(frases," "),"...","#"),"!","#"),"?","#"),".","#"),"#")
    separadas = list.remove(frase_separada,' ')
    return len(separadas)