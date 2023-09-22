def retira_pontuacao(frase):
    """A função receberá uma frase(string) como parâmetro
    e retornará a mesma frase porém toda a pontuação será
    substituída por espaço.
    Entrada: String
    Saída: String"""
    
    pontuacao = [',','-',':',';','.']
    frase_nova = str.replace(frase, pontuacao, ' ')
    return frase_nova