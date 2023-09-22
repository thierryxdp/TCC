vogais = ['a','e','i','o','u','á','é','í','ó','ú']

def linguado_p(palavra):
    palavrap = ""
    for i in range(len(palavra)):
        palavrap += palavra[i]
        for vogal in vogais:
            if palavra[i] == vogal:
                palavrap +=  "p" + vogal