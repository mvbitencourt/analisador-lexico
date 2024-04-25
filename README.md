# Analisador Léxico para Compiladores

## Descrição
Este repositório contém um analisador léxico implementado em Python, projetado para identificar e classificar tokens a partir de uma entrada de código-fonte conforme definido por uma tabela de transições de estados. O analisador utiliza um Autômato Finito Determinístico (DFA) para processar a entrada e identificar tokens como identificadores, palavras-chave, literais numéricos, operadores e delimitadores.

## Características
- **Tabela de Transições**: O DFA é baseado em uma tabela de transições detalhada que direciona o fluxo de processamento dos caracteres de entrada.
- **Estados de Aceitação**: Determinados estados são marcados como estados de aceitação, onde um token é oficialmente reconhecido.
- **Flexibilidade**: Capaz de reconhecer uma variedade de tokens, incluindo operadores, identificadores e palavras reservadas. Além disso, tambem gera relatórios dos tokens que foram gerados e do número de ocorrências de cada um.

## Estrutura do Projeto
O projeto é composto pelos seguintes arquivos principais:
- `analisador_lexico.py`: O script principal que contém a lógica do DFA e a tabela de transições.
- `entrada.txt`: Arquivo de texto que contém o código-fonte a ser analisado.
- `saida_tokens_gerados.txt`: Arquivo que lista todos os tokens reconhecidos durante a análise.
- `saida_ocorrencias_tokens.txt`: Arquivo que sumariza as ocorrências de cada tipo de token.
- `saida_erros.txt`: Arquivo que contém detalhes dos erros encontrados durante a análise léxica.

## Funcionamento
O analisador lê caracteres de entrada e, usando a função `verifica_caractere`, determina o tipo de caractere e a coluna correspondente na tabela de transições. A função `verifica_proximo_estado` é usada para determinar o próximo estado com base no estado atual e no tipo de caractere. Se um estado de aceitação é alcançado, um token correspondente é gerado. Caso não, o erro é registrado no arquivo de saída. Os outros métodos auxiliares presente no arquivo servem para formatação dos arquivos de saída.

## Uso
Para usar o analisador léxico, siga os passos abaixo:
1. Clone este repositório em sua máquina local.
2. Adicione o código-fonte que deseja analisar no arquivo `entrada.txt`.
3. Execute o script `analisador_lexico.py` usando Python:
4. Verifique os arquivos de saída `saida_tokens_gerados.txt`, `saida_ocorrencias_tokens.txt` e `saida_erros.txt` para visualizar os tokens reconhecidos, suas ocorrências e quaisquer erros de análise.