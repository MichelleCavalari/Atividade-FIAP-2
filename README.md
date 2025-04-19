# Sistema de Planejamento Agrícola - FIAP

Este projeto foi desenvolvido como parte da atividade avaliativa da disciplina de Fundamentos de Banco de Dados, com foco em **Agricultura Digital** e **otimização de recursos no Agronegócio**.

## Objetivo

A proposta do sistema é auxiliar pequenos produtores rurais no **planejamento da plantação de milho por hectare**, fazendo o cálculo de:

- Quantidade de sementes
- Insumos necessários
- Irrigação
- Mão de obra
- Custo total por hectare
- Estimativa do preço de venda
- Controle de estoque de insumos disponíveis

## Tecnologias Utilizadas

- Python 
- Oracle SQL 
- Pandas (para exibição dos dados)
- Prompt de comando para interação com o usuário
- Git & GitHub para versionamento e entrega

##  Lógica do Sistema

O sistema é interativo via terminal e consiste em um menu com operações CRUD (Criar, Ler, Atualizar, Deletar). Os dados são armazenados em uma tabela Oracle com as seguintes funcionalidades:

- Cadastrar cultura e estimativas por hectare
- Listar registros com DataFrame limpo e organizado
- Atualizar registros existentes
- Excluir registros individuais ou em massa
- Validar entradas do usuário para evitar erros de tipo

##  Relevância para o Agronegócio

O projeto trata diretamente de um problema real enfrentado por produtores: o **planejamento eficiente e preciso do plantio**. Ao facilitar os cálculos e armazenar os dados, o sistema contribui para:

- Tomada de decisão baseada em dados
- Redução de desperdícios
- Previsão de custos e lucros
- Sustentabilidade no uso de recursos

## Inovação

Mesmo com interface simples via terminal, o projeto demonstra inovação ao integrar:

- Banco de dados relacional com Python
- Cálculo de insumos personalizados
- Interação dinâmica com o produtor
- Estrutura de código modular e organizada

## 📁 Estrutura do Projeto

