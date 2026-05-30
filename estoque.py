from produto import Produto


class Estoque:

    def __init__(self):
        self.produtos = []

    def cadastrar(self, produto):

        if self.buscar_codigo(produto.codigo):
            return False

        self.produtos.append(produto)
        self.produtos.sort(key=lambda p: p.codigo)

        return True

    def buscar_codigo(self, codigo):

        inicio = 0
        fim = len(self.produtos) - 1

        while inicio <= fim:

            meio = (inicio + fim) // 2

            if self.produtos[meio].codigo == codigo:
                return self.produtos[meio]

            elif self.produtos[meio].codigo < codigo:
                inicio = meio + 1

            else:
                fim = meio - 1

        return None