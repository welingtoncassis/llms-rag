## Rag pdf document

### Descrição

Este projeto implementa um sistema de perguntas e respostas baseado em um documento PDF, utilizando a biblioteca LangChain. Ele carrega um arquivo PDF, divide o texto em pequenos segmentos (chunks), armazena esses segmentos em um banco de dados vetorial (Chroma) e utiliza um modelo de linguagem da OpenAI para responder perguntas com base no documento.

### Requisitos

Antes de executar o código, certifique-se de ter os seguintes pacotes instalados:

```bash
pip install langchain langchain-openai langchain-community chromadb pymupdf
```

### Configuração

1. Defina sua chave de API da OpenAI:

   ```python
   os.environ["OPENAI_API_KEY"] = "yourkey"
   ```

   Substitua `yourkey` pela sua chave de API da OpenAI.

2. Certifique-se de que o arquivo PDF desejado está no diretório do código e atualize a variável `pdf_link`:
   ```python
   pdf_link = "os-sertoes.pdf"
   ```

### Como Funciona

1. O documento PDF é carregado e seu texto é extraído.
2. O texto é dividido em chunks para melhor indexação e recuperação.
3. Os chunks são armazenados no banco de dados vetorial Chroma.
4. Quando o usuário faz uma pergunta, o sistema busca os chunks mais relevantes no banco de dados e usa um modelo de linguagem (LLM) para formular uma resposta.

### Como Executar

Execute o script Python e insira sua pergunta quando solicitado:

```bash
python script.py
```

Digite sua pergunta e aguarde a resposta baseada no documento PDF carregado.

### Estrutura do Código

- **Carregamento do PDF**: Extração do texto usando `PyMuPDFLoader`.
- **Divisão do texto**: Utiliza `RecursiveCharacterTextSplitter`.
- **Indexação**: O texto processado é armazenado no banco de dados vetorial Chroma.
- **Recuperação e resposta**: Um `retriever` busca os chunks mais relevantes para a pergunta e um `LLM` da OpenAI gera a resposta.

### Exemplo de Uso

```bash
User: Qual é a experiência profissional do candidato?
Answer: O candidato possui experiência em...
```

### Observação

- Substitua `yourkey` pela sua chave de API da OpenAI.
- O arquivo PDF deve estar no mesmo diretório do script ou deve-se especificar o caminho correto.
- Para persistência dos embeddings, o diretório `text_index` é criado automaticamente.
