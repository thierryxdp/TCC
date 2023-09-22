def conta_frases(s):
    char=['.',', ','! ','?','; ','-',':',' (',')','. ']
    texto=s.split()
    cont=0
    for laco in texto:
        for laco_char in char:
            if laco_char in laco:
                cont+=1
    return cont