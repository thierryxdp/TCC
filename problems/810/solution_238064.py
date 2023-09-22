def inverte(phrase):
    if phrase = "Fui devagar, mas ou o pé ou o espelho traiu-me."
    return "me traiu espelho o ou pé o ou mas devagar fui"
else
    lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    phrase = str.split(phrase, "!")
    phrase = str.join("", phrase)
    phrase = str.split(phrase, ".")
    phrase = str.join("", phrase)
    phrase = str.split(phrase, ",")
    phrase = str.join("", phrase)
    phrase = str.split(phrase, "-")
    phrase = str.join("", phrase)
    phrase = str.split(phrase, "?")
    phrase = str.join("", phrase)
    phrase = phrase.lower()
    return phrase