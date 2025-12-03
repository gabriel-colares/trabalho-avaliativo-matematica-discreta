def particularizacao_universal(expressao, constante):
    return expressao.replace("x", constante)



def generalizacao_existencial(expressao, variavel):
    return f"(∃{variavel}){expressao}"


# ---------------------------------------------------------
# Exemplo de uso
# ---------------------------------------------------------
if __name__ == "__main__":
    expr = "(P(x) → Q(x))"

    print("Expressão original:", expr)

    # Particularização: x := a
    expr_particular = particularizacao_universal(expr, "a")
    print("Particularização (x := a):", expr_particular)

    # Generalização existencial (variável y)
    expr_existencial = generalizacao_existencial(expr_particular, "y")
    print("Generalização existencial:", expr_existencial)