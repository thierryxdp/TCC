def retira_pontuacao(frase):
    '''rertira todas as pontuacoes de uma frase e substtituii por espacco'''
    travessao= frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoexclamacao = pontointerrogacao.replace('!', ' ')
    
    return pontoexclamacao





def inverte(frase):
    '''reetorna a mesma frase de entrada na ordem inveresa com todas as letras minussculas e semm pontuacao'''
    
    removepontuacao = retira_pontuacao(frase)
    minuscula = removepontuacao.lower()
    removeespaco = minuscula.strip()
    novafrasesplit = removeespaco.split()[::-1] 
    novafrasejoin = " ".join(novafrasesplit)
    return novafrasejoin