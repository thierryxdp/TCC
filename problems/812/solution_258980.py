def retira_pontuacao(frase):
    """A função receberá uma frase(string) como parâmetro
    e retornará a mesma frase porém toda a pontuação será
    substituída por espaço.
    Entrada: String
    Saída: String"""
    
    pont = '''-,.:;!?-''' 
    nopont = not[pont]
    frase_nova = (str.replace(frase, nopont, ' '))
    return frase_nova