def inverte(frase):
    minuscula= str.lower(frase)
    pontuacao= str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(minuscula,'-',' '),',',''),':',' '),';',' '),'.',' '),'?',' '),'!',' ')
    s= str.split(pontuacao,' ')[::-1]
    """dada uma frase, a função retorna a mesma frase, porém com algumas
    alterações:
    - sem pontuação
    - sem letras maiúsculas
    - com palavras na ordem inversa
    
    string-->string
    
    Parâmetros
    frase: frase de entrada que será alterada pela função"""
    return str.strip(str.join(' ', s))