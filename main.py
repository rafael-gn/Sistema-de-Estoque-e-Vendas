from estoque import Estoque
from produto import Produto
from arquivos import salvar, carregar


def mostrar_menu():
    print("\n=== SISTEMA DE ESTOQUE E VENDAS ===")
    print("1 - Cadastrar Produto")
    print("2 - Buscar Produto por Código")
    print("3 - Buscar Produto por Nome")
    print("4 - Editar Produto")
    print("5 - Remover Produto")
    print("6 - Registrar Venda")
    print("7 - Listar Produtos")
    print("8 - Salvar Dados")
    print("9 - Produtos por Categoria")
    print("10 - Relatório de Estoque Baixo")
    print("11 - Produto com Maior Preço")
    print("12 - Produto com Menor Preço")
    print("0 - Sair")


def main():

    estoque = Estoque()
    estoque.produtos = carregar()

    while True:

        mostrar_menu()

        opcao = input("\nEscolha uma opção: ")

        try:

            # CADASTRAR
            if opcao == "1":

                codigo = int(input("Código: "))
                nome = input("Nome: ")
                categoria = input("Categoria: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))

                if preco <= 0:
                    print("Preço deve ser positivo.")
                    continue

                if quantidade < 0:
                    print("Quantidade não pode ser negativa.")
                    continue

                produto = Produto(
                    codigo,
                    nome,
                    categoria,
                    preco,
                    quantidade
                )

                if estoque.cadastrar(produto):
                    print("Produto cadastrado com sucesso!")
                else:
                    print("Código já cadastrado.")
                    
            if estoque.cadastrar(produto):
                print("Produto cadastrado!")
                print(estoque.produtos)

            # BUSCAR POR CÓDIGO
            elif opcao == "2":

                codigo = int(input("Código: "))

                produto = estoque.buscar_codigo(codigo)

                if produto:
                    print(produto)
                else:
                    print("Produto não encontrado.")

            # BUSCAR POR NOME
            elif opcao == "3":

                nome = input("Nome: ")

                produtos = estoque.buscar_nome(nome)

                if produtos:
                    for produto in produtos:
                        print(produto)
                else:
                    print("Nenhum produto encontrado.")

            # EDITAR
            elif opcao == "4":

                codigo = int(input("Código do produto: "))

                nome = input("Novo nome: ")
                categoria = input("Nova categoria: ")
                preco = float(input("Novo preço: "))
                quantidade = int(input("Nova quantidade: "))

                if preco <= 0:
                    print("Preço deve ser positivo.")
                    continue

                if quantidade < 0:
                    print("Quantidade não pode ser negativa.")
                    continue

                if estoque.editar(
                    codigo,
                    nome,
                    categoria,
                    preco,
                    quantidade
                ):
                    print("Produto atualizado com sucesso!")
                else:
                    print("Produto não encontrado.")

            # REMOVER
            elif opcao == "5":

                codigo = int(input("Código: "))

                if estoque.remover(codigo):
                    print("Produto removido.")
                else:
                    print("Produto não encontrado.")

            # VENDA
            elif opcao == "6":

                codigo = int(input("Código: "))
                quantidade = int(input("Quantidade vendida: "))

                if estoque.vender(codigo, quantidade):
                    print("Venda registrada com sucesso!")
                else:
                    print("Estoque insuficiente ou produto inexistente.")

            # LISTAR
            elif opcao == "7":

                if not estoque.produtos:
                    print("Nenhum produto cadastrado.")
                else:
                    for produto in estoque.produtos:
                        print(produto)

            # SALVAR
            elif opcao == "8":

                salvar(estoque.produtos)
                print("Dados salvos com sucesso.")

            # PRODUTOS POR CATEGORIA
            elif opcao == "9":

                categoria = input("Categoria: ")

                produtos = estoque.listar_categoria(categoria)

                if produtos:
                    for produto in produtos:
                        print(produto)
                else:
                    print("Nenhum produto encontrado.")

            # ESTOQUE BAIXO
            elif opcao == "10":

                limite = int(input("Limite mínimo: "))

                produtos = estoque.estoque_baixo(limite)

                if produtos:
                    for produto in produtos:
                        print(produto)
                else:
                    print("Nenhum produto abaixo do limite.")

            # MAIOR PREÇO
            elif opcao == "11":

                produto = estoque.maior_preco()

                if produto:
                    print(produto)
                else:
                    print("Nenhum produto cadastrado.")

            # MENOR PREÇO
            elif opcao == "12":

                produto = estoque.menor_preco()

                if produto:
                    print(produto)
                else:
                    print("Nenhum produto cadastrado.")

            # SAIR
            elif opcao == "0":

                salvar(estoque.produtos)

                print("Dados salvos.")
                print("Sistema encerrado.")

                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Entrada inválida. Digite valores corretos.")

        except Exception as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()