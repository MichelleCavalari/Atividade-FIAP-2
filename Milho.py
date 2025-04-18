import json


# Função para carregar o estoque dos insumos
def carregar_estoque():
    try:
        with open('estoque.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {"sementes": 0, "fertilizante": 0, "defensivo": 0, "irrigacao": 0}


# Função para salvar o estoque
def salvar_estoque(estoque):
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)


# Função para exibir o estoque atual
def consultar_estoque(estoque):
    print("\nEstoque Atual:")
    for insumo, quantidade in estoque.items():
        print(f"{insumo.capitalize()}: {quantidade} unidades")


# Função para atualizar o estoque
def atualizar_estoque(estoque):
    insumo = input(
        "\nDigite o nome do insumo que deseja atualizar (sementes, fertilizante, defensivo, irrigacao): ").lower()
    if insumo in estoque:
        try:
            quantidade = int(input(f"Digite a quantidade de {insumo} para adicionar ao estoque: "))
            estoque[insumo] += quantidade
            print(f"Estoque de {insumo} atualizado para {estoque[insumo]} unidades.")
            salvar_estoque(estoque)
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("Insumo não encontrado. Escolha entre sementes, fertilizante, defensivo ou irrigação.")


# Função para calcular os custos
def calcular_custos():
    estoque = carregar_estoque()
    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar estoque")
        print("2. Atualizar estoque")
        print("3. Calcular custo da produção")
        print("4. Sair")

        opcao = input("Escolha a opção (1/2/3/4): ")

        if opcao == "1":
            consultar_estoque(estoque)
        elif opcao == "2":
            atualizar_estoque(estoque)
        elif opcao == "3":
            hectares = float(input("\nQuantos hectares você deseja plantar? "))
            custo_sementes = float(input("Qual o custo da saca de sementes (R$)? "))
            quantidade_sementes = float(input("Quantos quilos de sementes são necessários por hectare? "))
            custo_fertilizante = float(input("Qual o custo do fertilizante por hectare (R$)? "))
            custo_defensivo = float(input("Qual o custo do defensivo por hectare (R$)? "))
            custo_irrigacao = float(input("Qual o custo da irrigação por hectare (R$)? "))
            custo_mao_obra = float(input("Qual o custo da mão de obra por hectare (R$)? "))

            # Cálculo total por hectare
            custo_total_por_hectare = (
                                                  custo_sementes * quantidade_sementes) + custo_fertilizante + custo_defensivo + custo_irrigacao + custo_mao_obra
            custo_total = custo_total_por_hectare * hectares

            print(f"\nResumo dos custos para {hectares} hectares:")
            print(f"Custo de sementes: R$ {custo_sementes * quantidade_sementes}")
            print(f"Custo de fertilizante: R$ {custo_fertilizante}")
            print(f"Custo de defensivo: R$ {custo_defensivo}")
            print(f"Custo de irrigação: R$ {custo_irrigacao}")
            print(f"Custo de mão de obra: R$ {custo_mao_obra}")
            print(f"\nCusto total para {hectares} hectares: R$ {custo_total}")
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    calcular_custos()

