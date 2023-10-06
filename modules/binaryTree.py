class No:
    def __init__(self, valor, vertice):
        self.valor = valor
        self.vertice = vertice
        self.visitado = False
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor, vertice):
        if self.raiz is None:
            self.raiz = No(valor, vertice)
        else:
            self._inserir_recursivamente(self.raiz, valor, vertice)

    def _inserir_recursivamente(self, no_atual, valor, vertice): 
        if valor >= no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor, vertice)
            else:
                self._inserir_recursivamente(no_atual.direita, valor, vertice)
        elif valor <= no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor, vertice)
            else:
                self._inserir_recursivamente(no_atual.esquerda, valor, vertice)

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return None  # Valor não encontrado na árvore
        if valor == no_atual.valor:
            return no_atual  # Valor encontrado
        if valor < no_atual.valor:
            return self._buscar_recursivamente(no_atual.esquerda, valor)
        return self._buscar_recursivamente(no_atual.direita, valor)

    def em_ordem(self):
        return self._em_ordem_recursivamente(self.raiz)

    def _em_ordem_recursivamente(self, no):
        if no is not None:
            print(f"{no.valor} {no.vertice}")
            self._em_ordem_recursivamente(no.esquerda)
            self._em_ordem_recursivamente(no.direita)

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir(0, 1)
arvore.inserir(5, 14)
arvore.inserir(13, 15)
arvore.inserir(13, 27)
arvore.inserir(13, 28)
arvore.inserir(5, 40)
arvore.inserir(5, 41)
arvore.inserir(0, 50)

print("Em ordem:")
arvore.em_ordem()

valor_buscado = 5
no_encontrado = arvore.buscar(valor_buscado)
if no_encontrado:
    print(f"\nValor {valor_buscado} encontrado na árvore.")
else:
    print(f"\nValor {valor_buscado} não encontrado na árvore.")
