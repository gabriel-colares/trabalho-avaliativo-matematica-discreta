from parser_proposicional import parse_expr
from tabela_verdade import tabela_verdade
from formas_argumento import identificar_forma
from parser_predicados import parse_predicado
from avaliador_predicados import avaliar_predicados
from regras_inferencia import particularizacao_universal

def menu_proposicional():
    print("\n--- Lógica Proposicional ---")
    try:
        n = int(input("Número de premissas: "))
    except ValueError:
        print("Entrada inválida.")
        return

    premissas = []
    for i in range(n):
        p = input(f"Premissa {i+1}: ")
        premissas.append(p)
    conclusao = input("Conclusão: ")
    
    print("\nAnalisando...")
    ok, contra_exemplos = tabela_verdade(premissas, conclusao)
    forma = identificar_forma(premissas, conclusao)
    
    print("\n-------------------------------------------------")
    print("SAÍDA:")
    if ok:
        print("✓ ARGUMENTO VÁLIDO")
    else:
        print("✗ ARGUMENTO INVÁLIDO")
    
    print("Método: Tabela Verdade")
    print("Forma detectada:", forma)
    
    if ok:
        print("Justificativa: Em todas as linhas onde as premissas são verdadeiras, a conclusão também é verdadeira.")
    else:
        print("Justificativa: Existe pelo menos uma linha onde as premissas são verdadeiras mas a conclusão é falsa.")
        if len(contra_exemplos) > 0:
            print("Contra-exemplo encontrado:", contra_exemplos[0])

def menu_predicados():
    print("\n--- Lógica de Predicados (Básico) ---")
    dominio_str = input("Domínio (ex: a,b,c): ")
    dominio = dominio_str.replace(" ", "").split(",")
    
    try:
        n = int(input("Número de premissas: "))
    except ValueError:
        print("Entrada inválida.")
        return

    premissas = []
    for i in range(n):
        p = input(f"Premissa {i+1}: ")
        premissas.append(p)
    conclusao = input("Conclusão: ")
    
    ok, contra_exemplo = avaliar_predicados(premissas, conclusao, dominio)
    
    print("\n-------------------------------------------------")
    print("SAÍDA:")
    if ok:
        print("✓ ARGUMENTO VÁLIDO")
    else:
        print("✗ ARGUMENTO INVÁLIDO")
    
    print("Método: Enumeração em domínio finito")
    print("Justificativa: Para todas as interpretações possíveis no domínio dado, a conclusão segue das premissas.")
    print("Regra aplicada: Verificação exaustiva de modelos.")
    if not ok:
        print("Justificativa: Encontrada uma interpretação onde as premissas são verdadeiras e a conclusão é falsa.")
        if contra_exemplo:
            pass

def main():
    while True:
        print("\n=== SISTEMA DE VALIDAÇÃO LÓGICA ===")
        print("1 - Lógica Proposicional")
        print("2 - Lógica de Predicados")
        print("3 - Sair")
        op = input("> ")
        if op == "1":
            menu_proposicional()
        elif op == "2":
            menu_predicados()
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
