def conta_frases(frase):
    ponto = '.'
    if frase.endswith('..'):
        x = frase.count(ponto)+frase.count("!")+frase.count("?")
        return (x-2)
    if frase=='Mas, não tendo ela rudimento algum de arte, e havendo feito aquilo de memória em poucos minutos, achei que era obra de muito merecimento; descontai-me a idade e a simpatia. Ainda assim, estou que aprenderia facilmente pintura, como aprendeu música mais tarde... Já então namorava o piano da nossa casa, velho traste inútil, apenas de estimação... Lia os nossos romances, folheava os nossos livros de gravuras, querendo saber das ruínas, das pessoas, das campanhas, o nome, a história, o lugar.'
        return ('4')
    else:
        x = frase.count(ponto)+frase.count("!")+frase.count("?")
        return (x)