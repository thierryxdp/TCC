def retira_pontuacao(frase):
    """A função receberá uma frase(string) como parâmetro
    e retornará a mesma frase porém toda a pontuação será
    substituída por espaço.
    Entrada: String
    Saída: String"""
    
    pont = '!-,:;?.'
    frase_nova = frase.replace(pont,' ')
    return frase_nova