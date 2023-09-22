def conta_frases(frase):
    """ Retorna o número de frases presentes na variavél texto, string -> int """
    num_final = str.count(frase,'.');
    num_exclamacao = str.count(frase,'!');
    num_interrogacao = str.count(frase,'?');
    num_reticencias = str.count(frase,'...');
    if(num_reticencias==0):
        return num_final+num_exclamacao+num_interrogacao+num_reticencias;
    else:
        if(num_reticencias>=1):
            return num_final+num_exclamacao+num_interrogacao+num_reticencias-(num_reticencias*3);