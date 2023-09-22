def quant_frases(frase):
    return (len(str.split(frase,'!'))-1) + (len(str.split(frase,'?'))-1) + (len(str.split(frase,'.'))-1) + (len(str.split(frase,'...'))-1)