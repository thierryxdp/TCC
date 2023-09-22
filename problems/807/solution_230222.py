def conta_frases(s):
    """retorna o numero de frases da string recebida
    assinatura:string --> int"""
    str.count(s,"...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))