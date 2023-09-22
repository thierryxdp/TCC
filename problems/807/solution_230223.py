def conta_frases(s):
    """Função que retorna o número de frases de um texto
    assinatura: string --> int 
    """
    str.count(s,"...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))