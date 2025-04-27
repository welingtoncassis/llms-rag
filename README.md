# 📚 Projeto RAG com Re-Rank: Análise de "Os Sertões"

Este projeto implementa uma arquitetura RAG (Retrieval-Augmented Generation) com reranqueamento (reranking) para responder a perguntas específicas sobre o livro _"Os Sertões"_ de Euclides da Cunha.

Utilizamos um modelo LLM (ChatGPT), embeddings da OpenAI, uma base vetorial (ChromaDB) e um reranker da Cohere para otimizar a busca de trechos relevantes antes de gerar a resposta final.

---

## 🧠 O que é Rerank RAG?

- O Rerank RAG é uma evolução do RAG clássico.
- No RAG tradicional:
  Após buscar os documentos mais relevantes (top K), todos são usados diretamente para gerar a resposta.

- No Rerank RAG:
  Após buscar os documentos (top K), um reranker (modelo de aprendizado) reorganiza ou filtra os documentos.
  Somente os melhores (mais relevantes para a pergunta) são enviados para o LLM.

- Benefícios do Rerank RAG:
  Reduz o ruído no contexto.
  Melhora a qualidade e a precisão da resposta.
  Usa menos tokens (mais barato e rápido).

- No projeto:
  Recuperamos 10 documentos.
  O reranker da Cohere seleciona os 3 mais relevantes.
  O ChatGPT gera a resposta com base apenas nesses 3.

## 🔧 Como funciona o projeto

1. **Carregamento de ambiente:**  
   As variáveis de ambiente são carregadas usando `dotenv`.

2. **Carregamento do documento:**  
   O PDF de _"Os Sertões"_ é carregado e dividido em pequenas partes (chunks) de até 4000 caracteres.

3. **Indexação vetorial:**  
   Os chunks são embutidos usando o modelo `text-embedding-3-small` da OpenAI e armazenados em uma base vetorial (`ChromaDB`).

4. **Configuração do retriever inicial:**  
   O retriever inicial (`naive_retriever`) busca os 10 chunks mais semelhantes ao texto da pergunta.

5. **Re-Ranking com Contextual Compression:**  
   Em vez de usar todos os 10 resultados, o projeto utiliza um reranker (`CohereRerank`) que:

   - **Reavalia** os 10 chunks recuperados,
   - **Seleciona** apenas os 3 mais relevantes.

   Isso é feito com a classe `ContextualCompressionRetriever`, que comprime o contexto retornado, aumentando a precisão da resposta.

6. **Geração de resposta:**  
   Um prompt específico é montado com o contexto selecionado e a pergunta.  
   O ChatGPT (gpt-3.5-turbo) gera a resposta com até 500 tokens.

7. **Execução:**  
   As perguntas listadas no código são respondidas automaticamente e impressas no console.

---

## 🚀 Como rodar o projeto

1. Clone o repositório.
2. Instale as dependências necessárias:
   ```bash
   pip install langchain langchain-openai langchain-cohere langchain-community chromadb python-dotenv
   ```
