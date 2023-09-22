def inverte(frase):
    "A funcao recebe uma frase que retonara invertida e sem pontuacao"
    removepontos=retira_pontuacao(frase)
    fraseminuscula=removepontos.lower()
    removeespacos=fraseminuscula.strip()
    novafrasesplit=removeespacos.split()[::-1]
    novafrasejoin=" ".join(novafrasesplit)
    return novafrasejoin