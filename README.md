# README para Analisador Léxico
Visão Geral
Este Analisador Léxico é projetado para tokenizar o código-fonte de entrada em unidades compreensíveis (tokens) para processamento adicional em um compilador. O analisador é construído em torno de um autômato finito determinístico (DFA) descrito através de uma tabela de transição, reconhecendo vários tipos de tokens, incluindo identificadores, palavras-chave, números, operadores e mais.

Tabela de Transições
O núcleo do analisador léxico é a tabela de transição, que define como o analisador transita de um estado para outro com base no caractere de entrada. Os estados podem levar à geração de tokens ou a mais transições de estado até que um token possa ser resolvido.

Componentes Chave
Tabela de Transição (tabela): Uma matriz que representa as transições de estado. Cada estado tem regras específicas para mover-se para o próximo estado ou permanecer no mesmo, dependendo do caractere lido.
Estados de Aceitação (estados_aceitacao): Lista dos estados que são considerados finais ou de aceitação, onde um token é formado.
Tokens Possíveis (tokens): Lista que mapeia cada estado de aceitação a um token específico que é gerado quando tal estado é alcançado.
Caracteres Possíveis (possiveis_caracteres): Todos os caracteres que o analisador pode ler e processar, cada um associado a uma coluna específica na tabela de transições.
Palavras Reservadas (palavras_reservadas): Lista de palavras-chave que são reconhecidas e tratadas como tokens especiais.
Funcionamento
O analisador lê caracteres de entrada e, usando a função verifica_caractere, determina o tipo de caractere e a coluna correspondente na tabela de transições. A função verifica_proximo_estado é usada para determinar o próximo estado com base no estado atual e no tipo de caractere. Se um estado de aceitação é alcançado, um token correspondente é gerado.

Arquivos de Saída
Tokens Gerados: Arquivo que lista todos os tokens reconhecidos.
Ocorrências de Tokens: Sumariza quantas vezes cada tipo de token ocorreu.
Erros: Relata quaisquer erros encontrados durante a análise, como caracteres não reconhecidos ou sequências inválidas.
Como Usar
Configuração Inicial: Defina a tabela de transições, estados de aceitação, e listas de tokens e caracteres.
Execução: Execute o script para analisar o código-fonte de entrada. O script processará o texto e identificará tokens, armazenando os resultados nos arquivos de saída correspondentes.
