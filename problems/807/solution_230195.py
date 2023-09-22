def conta_frases(s):
    """Recebe um texto em string e retorna o número de frases dele.
    assinatura: string --> int 
    testes:
    conta_frases('Eu moro no Brasil! Sou carioca...') == 2
    conta_frases('Amo o Rio de Janeiro. Amo química! Estudo na UFRJ...') == 3
    """
    str.count(s,"...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))