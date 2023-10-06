class No:
    def __init__(self, valor, peso=0):
        self.valor = valor
        self.peso = peso
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor, valorFilho=0, peso=0 ):
        if self.raiz == None:
            self.raiz = No(valor, 0)
        
        noatual = self.buscar(valor)
        if noatual:
            if noatual.esquerda == None:
                noatual.esquerda = No(valorFilho, peso)
            elif noatual.direita == None:
                noatual.direita = No(valorFilho, peso)
            else:
                print('nao tem mais como adicionar')
                print(f"{noatual.valor} {noatual.esquerda.valor} {noatual.direita.valor}")
        else:
            print(f"este no nao se liga com ninguem {valor} {valorFilho}")
            
    def buscar(self, valor, no=None):
        if no is None:
            no = self.raiz

        if no is None:
            return None  # Árvore vazia

        if no.valor == valor:
            return no  # Valor encontrado

        # Recursivamente busca nos filhos esquerdo e direito, se existirem
        if no.esquerda:
            resultado_esquerda = self.buscar(valor, no.esquerda)
            if resultado_esquerda:
                return resultado_esquerda  # Encontrado na subárvore esquerda

        if no.direita:
            resultado_direita = self.buscar(valor, no.direita)
            if resultado_direita:
                return resultado_direita  # Encontrado na subárvore direita

        return None  # Valor não encontrado na árvore

    def em_ordem(self):
        return self._em_ordem_recursivamente(self.raiz)

    def _em_ordem_recursivamente(self, no):
        if no is not None:
            self._em_ordem_recursivamente(no.esquerda)
            print(f"Valor: {no.valor}, Peso: {no.peso}")
            self._em_ordem_recursivamente(no.direita)


# Exemplo de uso:

# arvore = ArvoreBinaria()
# arvore.inserir(1, 2, 5) # (VALOR, VALORfilho, PESO)
# arvore.inserir(2, 3, 5)

# print("Em ordem:")
# arvore.em_ordem()

# valor_buscado = 30
# no_encontrado = arvore.buscar(valor_buscado)
# if no_encontrado:
#     print(f"Valor {valor_buscado} encontrado na árvore. Peso: {no_encontrado.peso}")
# else:
#     print(f"Valor {valor_buscado} não encontrado na árvore.")
 