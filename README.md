# llms-rag

## O que é RAG (Retrieval-Augmented Generation)?
RAG (Retrieval-Augmented Generation) é uma abordagem que combina recuperação de informações com modelos de geração de linguagem (LLMs) para fornecer respostas mais precisas e contextuais. Em vez de confiar apenas no conhecimento pré-treinado do modelo, o RAG busca informações relevantes em uma base de dados antes de gerar uma resposta.

## Como funciona o RAG?
- Entrada do usuário: O usuário faz uma pergunta ou insere um prompt.
- Recuperação de contexto: O sistema busca documentos relevantes em uma base de conhecimento (banco vetorial, banco de dados, APIs, etc.).
- Geração aumentada: O modelo de linguagem (LLM) utiliza os dados recuperados para gerar uma resposta mais precisa e informada.
- Resposta ao usuário: O resultado final é apresentado, contendo informações extraídas do contexto recuperado.

Essa técnica melhora a precisão e confiabilidade das respostas, permitindo que os modelos respondam com base em informações externas e atualizadas.

## Exemplos de RAG

- [RAG para PDFs](rag-pdf-document/README.md): Exemplo de recuperação aumentada de geração aplicada a documentos PDF.