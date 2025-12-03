import re

def get_variables(exprss: str):
    return sorted(set(re.findall(r"[A-Za-z]", exprss)))

def parse_expr(exprss: str):
    exprss = exprss.replace(" ", "")
    exprss = exprss.replace("~", " not ")
    exprss = exprss.replace("&", " and ")
    exprss = exprss.replace("∧", " and ")
    exprss = exprss.replace("|", " or ")
    exprss = exprss.replace("∨", " or ")
    exprss = exprss.replace("->", " <= ")
    exprss = exprss.replace("<->", " == ")
    
    return exprss
