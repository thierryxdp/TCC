def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase e substitui
    por espaços
    valores: str --> str'''
    frase= frase.replace('.',' ')
    frase= frase.replace('!',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace(',',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    return frase

def inverte(frase):
    '''Função retorna a mesma frase só que com os elementos
    em ordem inversa, além de não ter letras maiusculas e 
    pontuação.
    Exemplo: 'Nossa, como eu gosto de chocolate'
    'chocolate de gosto como eu nossa'
    valores: str --> str'''
    frase= retira_pontuacao(frase)
    frase= frase.lower()
    frase= frase.strip()
    frase= frase.split()
    frase= frase[::-1]
    return str.join(' ', frase2)