class Produto:
    def __init__(self, codigo, descricao, categoria_produto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = None
        self.__preco_unitario = None
        self.__cliente = None
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @property
    def cliente(self):
        return self.__cliente
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        
    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        self.__categoria_produto = categoria_produto

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def preco_total(self):
        return self.__quantidade * self.__preco_unitario