def lingua_p(palavra):
    """Recebe como entrada uma string e retorna outra string
       com vogais mais a letra p mais a vogal original
       parâmetro de entrada:str
       parâmetro de saída:str"""
    palavra_tratada=''
    for caractere in palavra:
        if caractere in 'aeiou':
            caractere=str.lower(caractere+'p'+caractere)
            palavra_tratada=palavra_tratada+caractere
    return palavra_tratada