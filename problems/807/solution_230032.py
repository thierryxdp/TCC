def conta_frases(s):
    """Recebe um texto em string e retorna o número de frases dele.
    assinatura: string --> int 
    testes:
    conta_frases('Eu estudo na UFRJ! Curso Bacharelado em Química...') == 2
    conta_frases('Me chamo Estela. Amo química! Moro em São paulo... Estudo no Rio!') == 4
    """
    str.count(s,"...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))