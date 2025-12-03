# parser_predicados.py
# Pessoa 4

import re

def parse_predicado(expr):
    expr = expr.replace(" ", "")
    predicados = re.findall(r"[A-Za-z]+\([A-Za-z0-9,]+\)", expr)
    return predicados

def extrair_quantificadores(expr):
    quant = re.findall(r"\((∀|∃)([a-z])\)", expr)
    return quant
