class Fila:
    """
    Classe que representa uma fila (Queue) simples usando lista Python.
    """

    def __init__(self):
        """
        Inicializa uma fila vazia.
        """
        self._itens = []  # Lista interna que armazena os elementos da fila

    def enfileirar(self, item):
        """
        Adiciona um item ao final da fila.

        Parâmetros:
        item: O item a ser adicionado.
        """
        self._itens.append(item)
        print(f"Item '{item}' enfileirado com sucesso.")

    def desenfileirar(self):
        """
        Remove e retorna o primeiro item da fila.

        Retorna:
        O primeiro item da fila.

        Levanta:
        IndexError se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia. Nenhum item para desenfileirar.")
        item = self._itens.pop(0)
        print(f"Item '{item}' desenfileirado.")
        return item

    def espiar(self):
        """
        Retorna o primeiro item da fila sem removê-lo.

        Retorna:
        O primeiro item da fila.

        Levanta:
        IndexError se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia. Nenhum item para espiar.")
        return self._itens[0]

    def esta_vazia(self):
        """
        Verifica se a fila está vazia.

        Retorna:
        True se estiver vazia, False caso contrário.
        """
        return len(self._itens) == 0




fila = Fila()

# Enfileirando itens
fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")

# Espiando o primeiro item
print("Primeiro item:", fila.espiar())  # Deve mostrar "A"

# Desenfileirando itens
fila.desenfileirar()  # Remove "A"
fila.desenfileirar()  # Remove "B"

# Verificando se a fila está vazia
print("Fila vazia?", fila.esta_vazia())  # False

# Desenfileirando o último item
fila.desenfileirar()  # Remove "C"

# Agora a fila está vazia
print("Fila vazia?", fila.esta_vazia())  # True

# Testando erro ao espiar/desenfileirar de fila vazia
try:
    fila.espiar()
except IndexError as e:
    print("Erro:", e)

try:
    fila.desenfileirar()
except IndexError as e:
    print("Erro:", e)
