import re

def get_variables(expr: str):
    vars_found = re.findall(r"[A-Za-z]", expr)
    unique_vars = []
    for v in vars_found:
        if v not in unique_vars:
            unique_vars.append(v)
    return sorted(unique_vars)

def parse_expr(expr: str):
    expr = expr.replace(" ", "")
    expr = expr.replace("~", " not ")
    expr = expr.replace("&", " and ")
    expr = expr.replace("∧", " and ")
    expr = expr.replace("|", " or ")
    expr = expr.replace("v", " or ")
    expr = expr.replace("<->", " == ")
    expr = expr.replace("->", " <= ")
    return expr
