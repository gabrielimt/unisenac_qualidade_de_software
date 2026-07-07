# Aula 15 – Modelos de Maturidade

## Integrantes

- Gabrieli Morales Taborda

---

# 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|-----------|-----|----------|-----|
| Os requisitos são documentados? | X | | |
| Existe controle de mudanças? | | X | |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | X | | |
| Existe padronização para implementação de funcionalidades? | | X | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | X | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | X | | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | X | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | | X |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | X |

### Nível de maturidade estimado

**Gerenciado (Nível F no MPS.BR ou Nível 2 no CMMI)**

### Justificativa

O processo do LocalEats apresenta fortes características do nível Gerenciado. A equipe documenta requisitos, planeja tarefas e utiliza ferramentas de versionamento para organizar os artefatos (código e testes E2E com Playwright/BDD). Os testes são executados antes das entregas. Contudo, a ausência de métricas formais de qualidade, a falta de reuniões de retrospectivas periódicas e uma rastreabilidade apenas parcial impedem que o processo seja classificado como "Definido". As práticas existem de forma reativa e dependem do esforço individual, indicando que o processo é gerenciado por projeto, mas ainda não é institucionalizado ou metrificado.

---

# 2. Lacunas Identificadas

| Lacuna | Impacto |
|---------|----------|
| Ausência de indicadores ou métricas de qualidade | Dificulta o acompanhamento do número de defeitos encontrados e da saúde geral do projeto. |
| Falta de reuniões de retrospectiva | A equipe perde oportunidades valiosas de identificar falhas no processo de forma contínua e aplicar melhorias. |
| Rastreabilidade e controle de mudanças parciais | Torna difícil relacionar um bug em produção a um requisito específico ou a uma mudança de código recente. |

---

# 3. Propostas de Melhoria

| Melhoria | Benefício |
|-----------|-----------|
| Implementar métricas básicas de qualidade (ex: cobertura de testes, taxa de falha) | Permitirá decisões baseadas em dados e melhor acompanhamento da evolução da qualidade do projeto. |
| Instituir reuniões de retrospectiva curtas ao final de cada ciclo/sprint | Fomentar a cultura de melhoria contínua, permitindo que a equipe ajuste o processo rapidamente. |
| Padronizar o vínculo de Commits e Pull Requests às Issues no GitHub | Garantirá rastreabilidade total entre os requisitos de negócio e o código final implementado, aumentando o controle. |

---

## Conclusão

A avaliação indica que a equipe alcançou uma maturidade onde o trabalho é gerenciado, com testes automatizados e controle de versão ativos. Contudo, para evoluir rumo à excelência de processos (como os níveis mais altos do CMMI/MPS.BR), é crucial adotar práticas de monitoramento quantitativo e cultivar uma rotina estruturada de melhoria contínua.