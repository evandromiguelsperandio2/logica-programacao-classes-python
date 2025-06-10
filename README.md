# Projeto de Estruturas de Dados em Python

Este projeto implementa algumas estruturas de dados e conceitos de programação orientada a objetos em Python. As funcionalidades incluem implementação de classes como `Livro`, `Retangulo`, `Animal`, `Cachorro`, `Gato`, `Fila`, e o uso de **herança**, **polimorfismo**, **encapsulamento** e **sobrescrita de métodos**.

## Estruturas Implementadas

### 1. **Classe Livro com Controle de Empréstimo**

A classe `Livro` representa um livro e possui funcionalidades para controlar o status de empréstimo:

- **Atributos**:
  - `titulo` (str): Título do livro.
  - `autor` (str): Autor do livro.
  - `disponivel` (bool): Status do livro, True se disponível, False se emprestado.

- **Métodos**:
  - `emprestar()`: Empresta o livro, marcando-o como não disponível.
  - `devolver()`: Marca o livro como disponível.
  - `consultar_status()`: Retorna o status atual do livro (disponível ou emprestado).

### 2. **Classe Retângulo com Cálculo de Área e Perímetro**

A classe `Retangulo` representa um retângulo e oferece métodos para calcular sua área e perímetro:

- **Atributos**:
  - `largura` (float): Largura do retângulo.
  - `altura` (float): Altura do retângulo.

- **Métodos**:
  - `calcular_area()`: Retorna a área do retângulo (largura * altura).
  - `calcular_perimetro()`: Retorna o perímetro do retângulo (2 * (largura + altura)).

- **Validação**: Garante que os valores de largura e altura sejam positivos ao utilizar getters e setters.

### 3. **Herança: Animal, Cachorro e Gato**

As classes `Cachorro` e `Gato` herdam da classe base `Animal` e sobrescrevem o método `emitir_som()` para emitir sons específicos:

- **Classe Animal**: 
  - Atributo: `nome` (str): Nome do animal.
  - Método: `emitir_som()`: Método genérico para emitir som de animal.

- **Classes Filhas**:
  - `Cachorro`: Sobrescreve o método para emitir "Woof!".
  - `Gato`: Sobrescreve o método para emitir "Miau!".

### 4. **Polimorfismo: Processamento de Pedidos**

O exemplo de polimorfismo implementa a função `processar_pedido()` que aceita objetos das classes `ProdutoFisico`, `Servico` e `ProdutoDigital`. Cada classe implementa sua lógica própria de processamento do pedido através do método `processar()`:

- **Classes**:
  - `ProdutoFisico`: Processa pedidos de produtos físicos (gera etiqueta de envio).
  - `Servico`: Processa pedidos de serviços (agenda e notifica o prestador).
  - `ProdutoDigital`: Processa pedidos de produtos digitais (envia link de download).

### 5. **Fila (Queue) Simples**

A classe `Fila` implementa uma estrutura de fila utilizando uma lista Python. A classe possui as seguintes funcionalidades:

- **Métodos**:
  - `enfileirar(item)`: Adiciona um item ao final da fila.
  - `desenfileirar()`: Remove e retorna o primeiro item da fila. Levanta uma exceção se a fila estiver vazia.
  - `espiar()`: Retorna o primeiro item da fila sem removê-lo. Levanta uma exceção se a fila estiver vazia.
  - `esta_vazia()`: Retorna True se a fila estiver vazia, False caso contrário.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x

### Passos

1. Clone o repositório:
   git clone https://github.com/evandromiguelsperandio2/logica-programacao-classes-python.git
   
2. Navegue até a pasta do projeto:
  cd logica-programacao-classes-python

3. Execute os arquivos Python conforme necessário.
Exemplo:
python nome_do_arquivo.py



### Explicações:
- **Objetivo**: O arquivo `README.md` tem como objetivo descrever as funcionalidades do projeto, explicando as classes e seus métodos.
- **Estrutura**:
  - **Introdução**: Explica brevemente o projeto.
  - **Funcionalidades**: Descrição das classes e seus métodos.
  - **Execução**: Instruções para rodar o projeto localmente.
  - **Testes**: Como testar as funcionalidades, com exemplos de uso.
  - **Licença**: Caso o projeto tenha uma licença, você pode incluir essa seção.
