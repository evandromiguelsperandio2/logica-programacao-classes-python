class Animal:
    """
    Classe base que representa um animal genérico.
    """

    def __init__(self, nome):
        """
        Inicializa o animal com um nome.

        Parâmetros:
        nome (str): Nome do animal.
        """
        self.nome = nome

    def emitir_som(self):
        """
        Método genérico para emitir som.
        Deve ser sobrescrito pelas subclasses.
        """
        print(f"{self.nome} faz um som.")

#SUBCLASSE CACHORRO
class Cachorro(Animal):
    """
    Classe que representa um cachorro, herda de Animal.
    """

    def emitir_som(self):
        """
        Sobrescreve o método emitir_som da classe Animal.
        """
        print(f"{self.nome} diz: Woof!")

#SUBCLASSE GATO
class Gato(Animal):
    """
    Classe que representa um gato, herda de Animal.
    """

    def emitir_som(self):
        """
        Sobrescreve o método emitir_som da classe Animal.
        """
        print(f"{self.nome} diz: Miau!")
        

# Criando os objetos
animal_generico = Animal("Criatura")
dog = Cachorro("Rex")
cat = Gato("Mimi")

# Chamando os métodos
animal_generico.emitir_som()  # Saída: Criatura faz um som.
dog.emitir_som()              # Saída: Rex diz: Woof!
cat.emitir_som()              # Saída: Mimi diz: Miau!
