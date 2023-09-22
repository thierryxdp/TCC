def retira_pontuacao(frase):
    """funao que substitui os caracteres de uma determinada frase por um espaco"""
    fraseNova=frase.replace('-','	')
    fraseNova=frase.replace(',','	')
    fraseNova=frase.replace(':','	')
    fraseNova=frase.replace(';','	')
    fraseNova=frase.replace('.','	')
    return fraseNova