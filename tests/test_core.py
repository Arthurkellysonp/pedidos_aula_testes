from core import cadastrar_produto, finalizar_pedido, produtos, pedidos
from estoque import estoque

def setup_function():
    produtos.clear()
    pedidos.clear()
    estoque.clear()

def test_cadastrar_produto_sucesso():
    result = cadastrar_produto("001", "Pizza", 30.0, 10)
    assert result is True
    assert "001" in produtos
    assert estoque["001"] == 10

def test_cadastrar_produto_existente():
    cadastrar_produto("001", "Pizza", 30.0, 10)
    result = cadastrar_produto("001", "Pizza", 30.0, 10)
    assert result is False

def test_finalizar_pedido_sucesso():
    cadastrar_produto("001", "Pizza", 30.0, 10)
    total = finalizar_pedido("001", 2)
    assert total == 60.0
    assert estoque["001"] == 8
    assert len(pedidos) == 1

def test_finalizar_pedido_estoque_insuficiente():
    cadastrar_produto("002", "Refrigerante", 5.0, 1)
    total = finalizar_pedido("002", 5)
    assert total is None

def test_finalizar_pedido_produto_inexistente():
    total = finalizar_pedido("999", 1)
    assert total is None
