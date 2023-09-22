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
    batata = str.join(batata[-1])
    return batata