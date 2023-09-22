def inverte(x):
    
    def remove_pontuacao(x):
    new_string = x
    new_string = new_string.replace(".",'')
    new_string = new_string.replace(",",'')
    new_string = new_string.replace(";",'')
    new_string = new_string.replace(":",'')
    new_string = new_string.replace("!",'')
    new_string = new_string.replace("?",'')
    new_string = new_string.replace("-",'')
    return new_string