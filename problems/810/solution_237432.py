def inverte(frase):
    removepontuacao = retira_pontuacao(frase)
    minuscula = removepontuacao.lower()
    removeespaco = minuscula.strip()
    novafrasesplit = removeespaco.split()[::-1] 
    novafraasejoin = " ".join(novafrasesplit)
    return novafrasejoin