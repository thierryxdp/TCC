def conta_frases(s):
    """Recebe um texto em string e retorna o número de frases dele.
    assinatura: string --> int 
    testes:
    conta_frases('Boa noite! Até amanhã...') == 2
    conta_frases(Sou de Recife. Oh linda ! Morena Tropicana ... eu quero teu sabor!') == 4
    """
    str.count(s,"...")
    s2 = str.replace(s,"...", '#######')
    str.count(s2,".")
    str.count(s2,"!")
    str.count(s2,"?")
    return (str.count(s,"...") + str.count(s2,"!") + str.count(s2,".") + str.count(s2,"?"))