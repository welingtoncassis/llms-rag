📌 O que é Parent RAG?

O Parent RAG é uma abordagem que melhora a recuperação de informações no RAG tradicional ao introduzir uma relação entre documentos pais e filhos. Em vez de dividir o documento em pequenos fragmentos e buscar nesses fragmentos individualmente, o Parent RAG mantém os documentos pais maiores e seus respectivos filhos menores, garantindo que a recuperação de contexto seja mais coerente e menos fragmentada.

🔹 Benefícios do Parent RAG em relação ao RAG tradicional:

- Melhor coerência: Retorna trechos mais completos e menos desconexos.

- Menos perda de contexto: O relacionamento entre documentos pais e filhos mantém a integridade da informação.

- Recuperação mais eficiente: Em vez de buscar apenas nos fragmentos individuais, a consulta recupera um bloco maior de contexto relevante.

- Maior precisão: Reduz a chance de respostas imprecisas devido à fragmentação excessiva do texto.

📄 Este projeto implementa um sistema de RAG (Retrieval-Augmented Generation) utilizando LangChain, ChromaDB e OpenAI para processar documentos em PDF e responder perguntas baseadas no seu conteúdo.

🛠️ Tecnologias Utilizadas

- LangChain: Framework para criar aplicações baseadas em LLMs.

- ChromaDB: Banco de dados vetorial para armazenar embeddings.

- OpenAI GPT-3.5 Turbo: Modelo de linguagem para geração de respostas.

- PyPDFLoader: Biblioteca para carregar e processar arquivos PDF.

📌 Funcionalidades

- Carrega um PDF e divide o texto em documentos pais e filhos.

- Armazena embeddings dos textos no ChromaDB.

- Recupera informações relevantes com ParentDocumentRetriever.

- Usa GPT-3.5 Turbo para responder perguntas baseadas no documento.

🎯 Como Executar

- Instale as dependências:

``` pip install langchain langchain_openai langchain_chroma chromadb pypdf ```

- Configure sua chave da OpenAI:

``` export OPENAI_API_KEY="sua-chave-aqui" ```

- Execute o script principal.
