def lingua_p(palavra):
    for vogal in "AEIOUaeiou":
        palavra=str.replace(palavra,vogal,vogal+"p"+vogal)
    return palavra