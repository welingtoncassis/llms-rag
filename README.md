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
- [RAG para code review](rag-code-review/README.md): Exemplo RAG para code review

## Chunks e overlap
No contexto de Retrieval-Augmented Generation (RAG), há algumas preocupações importantes a serem consideradas com relação ao tamanho do chunk (E chunk size) e a sobreposição dos chunks (Q chunk overlap):

### Tamanho do Chunk (E chunk size):
- Chunks Pequenos: Menores chunks permitem incluir mais informações no contexto, mas podem resultar em falta de contexto suficiente para a compreensão completa.

- Chunks Grandes: Maiores chunks fornecem mais contexto, mas podem incluir informações irrelevantes, diluindo a qualidade da saída.

- Equilíbrio: O desafio é encontrar um tamanho de chunk que equilibre a quantidade de informações relevantes e a eficiência do processamento.

### Sobreposição dos Chunks (Q chunk overlap):

- Sobreposição: A sobreposição garante que informações importantes não sejam perdidas entre chunks consecutivos, preservando o contexto.

- Sem Sobreposição: Sem sobreposição, pode haver lacunas de contexto que afetam a precisão das respostas geradas.

- Configuração Adequada: Ajustar a sobreposição corretamente é crucial para manter a continuidade e a relevância das informações.

## Desafios do RAG
### Latência e Performance
O processo de buscar documentos relevantes antes de gerar uma resposta pode aumentar o tempo de resposta.
Indexação e recuperação eficientes exigem um bom balanceamento entre precisão e velocidade.

### Qualidade da Recuperação
Se os documentos recuperados não forem relevantes ou estiverem desatualizados, o modelo pode gerar respostas erradas.
A eficácia da busca depende da qualidade dos embeddings e da estratégia de recuperação (ex.: BM25, FAISS).

### Alucinações do Modelo Generativo
Mesmo com boas informações recuperadas, o LLM pode interpretar mal ou gerar informações incorretas.
A fusão entre as informações buscadas e a resposta gerada pode introduzir imprecisões.

### Manutenção da Base de Conhecimento
Atualizar os dados indexados para garantir informações recentes pode ser um desafio técnico.
Dependendo do volume de dados, a reindexação pode ser cara e demorada.

### Contexto e Limites de Memória
A limitação do contexto do modelo pode impedir que ele processe um grande número de documentos recuperados.
Estratégias como sumarização ou ranqueamento dos documentos precisam ser bem ajustadas.
Limitações do RAG


### Dependência de Dados Externos
Se os documentos disponíveis forem insuficientes ou tendenciosos, o modelo gerará respostas enviesadas ou incompletas.


### Dificuldade com Respostas Síntese
Se a resposta ideal exige consolidar informações de múltiplas fontes, o modelo pode falhar ao conectá-las corretamente.

### Segurança e Privacidade
Dependendo dos dados utilizados na recuperação, pode haver riscos de exposição de informações sensíveis.
Garantir que documentos privados não sejam indevidamente usados na geração é um desafio.
