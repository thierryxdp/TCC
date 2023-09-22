def lingua_p(palavra):
    """Essa função serve para traduzir uma palavra para a língua do p
    str->str"""
    v = "aáàâãeéèêêiíìîoóòôõuúùû"
    palavra = palavra.lower()
    nova_palavra = ""
    for letra in palavra:
        nova_palavra += letra
        if letra in v:
            nova_palavra += "p" + letra
    return nova_palavra


#lingua_p("Abóbora") == 'apabópóboporapa'
#lingua_p("Opa") == 'opopapa'
#lingua_p("Macabu") == 'mapacapabupu'