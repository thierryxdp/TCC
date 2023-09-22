def lingua_p(string):
    vogal = "AEIOUaeiou"
    for contador in len(string):
        if string[contador] in vogal:
            converter = string[contador] + "p" + string[contador] + string[contador+1:]
        return converter