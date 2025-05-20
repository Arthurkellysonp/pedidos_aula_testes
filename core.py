from estoque import verificar_estoque, estoque
from logger import logger

produtos = {}
pedidos = []

def cadastrar_produto(produto_id, nome, preco_unitario, quantidade_estoque):
    try:
        if produto_id in produtos:
            raise ValueError("Produto já cadastrado.")
        
        produtos[produto_id] = {
            "nome": nome,
            "preco_unitario": preco_unitario
        }
        estoque[produto_id] = quantidade_estoque
        logger.info(f"Produto '{nome}' cadastrado com sucesso.")
        return True
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {e}")
        return False

def finalizar_pedido(produto_id, quantidade, desconto=0):
    try:
        if produto_id not in produtos:
            raise ValueError("Produto não encontrado.")
        
        if not verificar_estoque(produto_id, quantidade):
            raise RuntimeError("Estoque insuficiente.")
        
        preco_unitario = produtos[produto_id]["preco_unitario"]
        total = preco_unitario * quantidade * (1 - desconto)
        
        pedidos.append({
            "produto_id": produto_id,
            "quantidade": quantidade,
            "total": total
        })
        estoque[produto_id] -= quantidade
        logger.info(f"Pedido finalizado: {quantidade}x '{produtos[produto_id]['nome']}' | Total: R${total:.2f}")
        return total
    except Exception as e:
        logger.error(f"Erro ao finalizar pedido: {e}")
        return None
