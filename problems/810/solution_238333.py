def retira_pontuacao(frase):
    "A funcao recebe uma frase pontuada e retorna toda a pontuacao substituida por espaco"
    travessao=frase.replace('-',' ')
    virgula=travessao.replace(',',' ')
    doispontos=virgula.replace(':',' ')
    pontovirgula=doispontos.replace(';',' ')
    pontofinal=pontovirgula.replace('.',' ')
    pontointerrogacao=pontofinal.replace('?',' ')
    pontoexclamacao=pontointerrogacao.replace('!',' ')
    return pontoexclamacao

def inverte(frase):
    "A funcao recebe uma frase que retonara invertida e sem pontuacao"
    removepontos=retira_pontuacao(frase)
    fraseminuscula=removepontos.lower()
    removeespacos=fraseminuscula.strip()
    novafrasesplit=removeespacos.split()[::-1]
    novafrasejoin=" ".join(novafrasesplit)
    return novafrasejoin