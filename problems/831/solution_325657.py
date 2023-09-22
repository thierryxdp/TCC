def lingua_p(palavra):
    """Retorna a palavra traduzida para a lingua do P:
       a cada vogal da palavra original é inserida a sequência de letra 'p'
       mais a vogal original;
       str->str
       Parâmentro:
       palavra: uma palavra qualquer
    """
    minu=str.lower(palavra)
    
    for letra in minu:  
        if letra in'aeiouã':
            lingua=letra+'p'+letra
            minu=str.replace(minu,letra,lingua)
            
    return minu