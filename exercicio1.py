class Livro:
    """
    Classe que representa um livro em uma biblioteca, com controle de empréstimo.
    """

    def __init__(self, titulo, autor):
        """
        Inicializa um novo livro com título, autor e disponibilidade.
        
        Parâmetros:
        titulo (str): O título do livro.
        autor (str): O autor do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # O livro está disponível por padrão

    def emprestar(self):
        """
        Realiza o empréstimo do livro, se estiver disponível.
        Caso contrário, informa que o livro já está emprestado.
        """
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado com sucesso.')
        else:
            print(f'O livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        """
        Devolve o livro, tornando-o disponível novamente.
        """
        self.disponivel = True
        print(f'O livro "{self.titulo}" foi devolvido com sucesso.')

    def consultar_status(self):
        """
        Consulta o status atual de disponibilidade do livro.

        Retorna:
        str: "Disponível" se o livro estiver disponível, "Emprestado" caso contrário.
        """
        return "Disponível" if self.disponivel else "Emprestado"

# Criando um livro
livro1 = Livro("Dom Casmurro", "Machado de Assis")

# Consultando status inicial
print("Status:", livro1.consultar_status())  # Deve exibir: Disponível

# Tentando emprestar o livro 1
livro1.emprestar()  # Deve exibir mensagem de sucesso

# Tentando emprestar novamente
livro1.emprestar()  # Deve informar que já está emprestado

# Devolvendo o livro 1
livro1.devolver()  # Deve exibir mensagem de devolução

# Consultando status final
print("Status:", livro1.consultar_status())  # Deve exibir: Disponível
