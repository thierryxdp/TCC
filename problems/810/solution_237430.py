def inverte(frase):
    removepontuacao = retirapontuacaco(frase)
    minuscula = removepontuacao.lower()
    removeespaco = minuscula.strip()
    novafrasesplit = removeespaco.split()[::-1] 
    novafraasejoin = " ".join(novafrasesplit)
    return novafrasejoin