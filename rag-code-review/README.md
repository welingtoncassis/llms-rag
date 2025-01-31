# RAG Code Review

Este repositório implementa um sistema de revisão de código utilizando técnicas de Recuperação Aumentada por Geração (RAG) e modelos de linguagem da OpenAI. Ele carrega códigos de um repositório Git, processa os arquivos e permite a análise do conteúdo por meio de consultas estruturadas.

## Funcionalidades
- Clonagem e carregamento de repositórios Git
- Extração e segmentação de código-fonte em pequenos blocos
- Armazenamento de embeddings vetoriais para recuperação eficiente de informação
- Integração com OpenAI GPT-3.5 Turbo para análise e revisão de código

## Dependências
Antes de executar o projeto, instale as dependências necessárias:

```bash
pip install langchain langchain_community langchain_chroma langchain_openai gitpython
```

## Como Executar
1. **Configurar a chave da OpenAI**:
   No arquivo `os.environ["OPENAI_API_KEY"]`, substitua a string vazia por sua chave da OpenAI.

2. **Executar o script**:
   
   ```bash
   python script.py
   ```

## Estrutura do Código

- **Clonagem do Repositório**: O código clona ou atualiza um repositório Git contendo os arquivos a serem analisados.
- **Carregamento de Arquivos**: Os arquivos Python são carregados e processados.
- **Segmentação do Código**: O código é dividido em pequenos blocos para facilitar a análise.
- **Criação de Banco de Dados Vetorial**: Os segmentos de código são armazenados em um banco vetorial usando ChromaDB.
- **Configuração do Modelo de Linguagem**: O GPT-3.5 Turbo é usado para realizar a análise e revisão do código.
- **Execução de Consulta**: O sistema permite consultar e obter sugestões de melhoria para trechos específicos de código.

## Exemplo de Uso

Para revisar o método `ask`, basta executar:

```python
response = retieval_chain.invoke({"input": "Voce pode revisar o código e sugerir melhorias no código do método ask?"})
print(response['answer'])
```

## Licença
Este projeto é licenciado sob a MIT License.