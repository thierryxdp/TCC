def contaf(frase):
    virgula= str.replace(frase,',',' ')
    travessao= str.replace(frase,'-',' ')
    dois_pt= str.replace(frase,':',' ')
    pt_virula= str.replace(frase,';',' ')
    ponto= str.replace(frase,'.',' ')
    if ',' in frase:
        return str.replace(virgula,'.',' ')
    elif '-' in frase:
        return str.replace(travessao,'.',' ')
    elif ':' in frase:
        return str.replace (dois_pt,'.',' ')
    elif ';' in frase:
        return str.replace(pt-virgula,'.',' ')
    else:
        return ponto