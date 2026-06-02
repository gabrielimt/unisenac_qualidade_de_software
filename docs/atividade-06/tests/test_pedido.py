import pytest
from pedido import calcular_total_pedido

# Teste 1
def test_deve_calcular_total_igual_ao_minimo():
    itens = [{"preco": 10}, {"preco": 5}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 15

# Teste 2
def test_deve_calcular_total_acima_do_minimo():
    itens = [{"preco": 20}, {"preco": 15}]
    valor_minimo = 25

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 35

# Teste 3
def test_deve_gerar_erro_quando_valor_abaixo_do_minimo():
    itens = [{"preco": 10}]
    valor_minimo = 20

    with pytest.raises(ValueError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo)