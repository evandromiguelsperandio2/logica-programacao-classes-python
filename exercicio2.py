class Retangulo:
    """
    Classe que representa um retângulo com métodos para cálculo de área e perímetro.
    """

    def __init__(self, largura, altura):
        """
        Inicializa o retângulo com largura e altura.
        
        Parâmetros:
        largura (float): A largura do retângulo (deve ser positiva).
        altura (float): A altura do retângulo (deve ser positiva).
        """
        self.set_largura(largura)
        self.set_altura(altura)

    def calcular_area(self):
        """
        Calcula a área do retângulo.

        Retorna:
        float: A área (largura * altura).
        """
        return self.__largura * self.__altura

    def calcular_perimetro(self):
        """
        Calcula o perímetro do retângulo.

        Retorna:
        float: O perímetro (2 * (largura + altura)).
        """
        return 2 * (self.__largura + self.__altura)

    # Getter para largura
    def get_largura(self):
        """
        Retorna a largura do retângulo.
        """
        return self.__largura

    # Setter para largura com validação
    def set_largura(self, largura):
        """
        Define a largura do retângulo, garantindo que seja um valor positivo.
        
        Parâmetros:
        largura (float): O novo valor da largura.
        """
        if largura > 0:
            self.__largura = largura
        else:
            raise ValueError("A largura deve ser um valor positivo.")

    # Getter para altura
    def get_altura(self):
        """
        Retorna a altura do retângulo.
        """
        return self.__altura

    # Setter para altura com validação
    def set_altura(self, altura):
        """
        Define a altura do retângulo, garantindo que seja um valor positivo.
        
        Parâmetros:
        altura (float): O novo valor da altura.
        """
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("A altura deve ser um valor positivo.")


# Criando um retângulo com largura 5 e altura 3
ret = Retangulo(5, 3)

# Exibindo área e perímetro
print("Área:", ret.calcular_area())           # Saída: 15
print("Perímetro:", ret.calcular_perimetro()) # Saída: 16

# Alterando os valores com os setters
ret.set_largura(10)
ret.set_altura(4)

print("Nova área:", ret.calcular_area())           # Saída: 40
print("Novo perímetro:", ret.calcular_perimetro()) # Saída: 28

# Testando validação
# ret.set_largura(-2)  # Isso causaria um ValueError
