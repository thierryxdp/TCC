def inverte(frase):
    batata = str.replace(frase, ".",' ')
    batata = str.replace(batata, "!",' ')
    batata = str.replace(batata, "?",' ')
    batata = str.replace(batata, ",",' ')
    batata = str.replace(batata, "-",' ')
    batata = str.replace(batata, ":",' ')
    batata = str.replace(batata, ";",' ')
    batata = str.replace(batata, "...",' ')
    batata = str.split(batata)
    return batata