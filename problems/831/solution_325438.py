def lingua_p(string):
    for vogal in "aeiou":
        strin=str.replace(string,vogal,vogal+"p"+vogal)
    return string