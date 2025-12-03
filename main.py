from parser_proposicional import parse_expr
from tabela_verdade import tabela_verdade
from formas_argumento import identificar_forma
from parser_predicados import parse_predicado, extrair_quantificadores
from avaliador_predicados import avaliar_predicados
from regras_inferencia import particularizacao_universal

def menu_proposicional():
    n = int(input("Número de premissas: "))
    premissas = [input(f"Premissa {i+1}: ") for i in range(n)]
    conclusao = input("Conclusão: ")
    ok = tabela_verdade(premissas, conclusao)
    forma = identificar_forma(premissas, conclusao)
    print("\nResultado:")
    print("Forma do argumento:", forma)
    print("Válido?" , "SIM" if ok else "NÃO")

def menu_predicados():
    dominio = input("Domínio (ex: a,b,c): ").split(",")
    n = int(input("Número de premissas: "))
    premissas = [input(f"Premissa {i+1}: ") for i in range(n)]
    conclusao = input("Conclusão: ")
    ok = avaliar_predicados(premissas, conclusao, dominio)
    print("\nResultado:")
    print("Válido?" , "SIM" if ok else "NÃO")

def main():
    while True:
        print("\n=== VERIFICADOR LÓGICO ===")
        print("1 - Lógica proposicional")
        print("2 - Lógica de predicados")
        print("3 - Sair")
        op = input("> ")
        if op == "1":
            menu_proposicional()
        elif op == "2":
            menu_predicados()
        elif op == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
