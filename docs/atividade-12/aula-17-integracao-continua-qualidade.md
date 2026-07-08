# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Gabrieli Morales Taborda

---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localeats-ci-qa |
| Link do repositório | https://github.com/gabrielimt/localeats-ci-qa |

### Estrutura de Diretórios

```text
localeats-ci-qa/
├── tests/
│   ├── features/
│   │   └── order_total.feature
│   ├── test_order_bdd.py
│   └── test_order.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── order.py
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a soma dos itens do pedido para o cliente |
| Link da Issue | https://github.com/gabrielimt/localeats-ci-qa/issues/1 |

*(Nota: Lembre-se de criar a Issue #1 no seu GitHub para que o link funcione)*

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário e BDD |
| Objetivo do teste | Verificar o cálculo correto do valor total do pedido |
| Link para o arquivo do teste | [test_order.py](https://github.com/gabrielimt/localeats-ci-qa/blob/main/tests/test_order.py) <br> [test_order_bdd.py](https://github.com/gabrielimt/localeats-ci-qa/blob/main/tests/test_order_bdd.py) |

**Código do Teste Unitário (`test_order.py`):**
```python
from order import calculate_total

def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60
```

**Código do Teste BDD (`test_order_bdd.py`):**
```python
from pytest_bdd import scenarios, given, when, then, parsers
from order import calculate_total

scenarios('features/order_total.feature')

@given(parsers.parse('que eu adicionei itens com os valores {val1:d}, {val2:d} e {val3:d} ao pedido'), target_fixture='items')
def order_items(val1, val2, val3):
    return [val1, val2, val3]

@when('o sistema calcula o valor total', target_fixture='total')
def calculate(items):
    return calculate_total(items)

@then(parsers.parse('o resultado retornado deve ser {expected_total:d}'))
def verify_total(total, expected_total):
    assert total == expected_total
```

**Arquivo Gherkin (`order_total.feature`):**
```gherkin
Feature: Cálculo do valor total do pedido
  Como um cliente do LocalEats
  Eu quero que o sistema calcule a soma dos itens do meu pedido
  Para que eu saiba o valor exato que devo pagar

  Scenario: Soma exata dos itens do pedido
    Given que eu adicionei itens com os valores 10, 20 e 30 ao pedido
    When o sistema calcula o valor total
    Then o resultado retornado deve ser 60
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o arquivo do workflow | https://github.com/gabrielimt/localeats-ci-qa/blob/main/.github/workflows/quality.yml |
| Link de uma execução do workflow | https://github.com/gabrielimt/localeats-ci-qa/actions |

**Código do workflow (`quality.yml`):**
```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install -r requirements.txt

      - run: pytest
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 2 |
| Quantidade de testes aprovados | 2 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro no cálculo do valor total do pedido |
| Severidade | Alta |
| Link da Issue | https://github.com/gabrielimt/localeats-ci-qa/issues/2 |

*(Nota: Lembre-se de criar a Issue #2 no seu GitHub para que o link funcione)*

**Descrição:**
O defeito foi simulado alterando a função `calculate_total` para retornar um valor incorreto de propósito. O erro foi identificado instantaneamente pela falha dos testes automatizados durante a execução do pipeline de Integração Contínua (GitHub Actions). O problema foi corrigido restaurando a lógica original da função (`return sum(items)`), o que fez os testes passarem novamente no *push* seguinte.