class ItemPedido:
    """
    Classe base para itens de pedido. Pode ser usada como interface comum.
    """
    def processar(self):
        """
        Método genérico de processamento.
        Deve ser sobrescrito pelas subclasses.
        """
        raise NotImplementedError("O método processar() deve ser implementado pelas subclasses.")




class ProdutoFisico(ItemPedido):
    def processar(self):
        print("Processando produto físico: gerar etiqueta de envio.")

class Servico(ItemPedido):
    def processar(self):
        print("Processando serviço: agendar e notificar o prestador.")

class ProdutoDigital(ItemPedido):
    def processar(self):
        print("Processando produto digital: enviar link de download por e-mail.")




def processar_pedido(item):
    """
    Processa um pedido chamando o método processar do item,
    independente do seu tipo específico.

    Parâmetros:
    item (ItemPedido): Um objeto que implementa o método processar().
    """
    item.processar()



# Criando instâncias dos diferentes tipos de pedido
produto = ProdutoFisico()
servico = Servico()
digital = ProdutoDigital()

# Processando todos usando a mesma função
processar_pedido(produto)   # Saída: Processando produto físico: gerar etiqueta de envio.
processar_pedido(servico)   # Saída: Processando serviço: agendar e notificar o prestador.
processar_pedido(digital)   # Saída: Processando produto digital: enviar link de download por e-mail.
