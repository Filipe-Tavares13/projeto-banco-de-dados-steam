# Projeto de Banco de Dados I - Fase 01 (Descoberta e Requisitos)

## 1. Fluxo do Trabalho Executado 
1. **Identificação e Coleta (API):** Utilizámos a API pública da **SteamSpy** (`top100in2weeks`) via script em Python para recolher dados reais dos 100 jogos mais jogados nas últimas duas semanas, guardando o retorno bruto em `dados_originais_steam.json`.
2. **Análise Preliminar e Limpeza:** Analisámos a estrutura do JSON, mapeamos o dicionário de dados e criamos uma rotina no script em Python para corrigir problemas (conversão de preços de cêntimos para dólares, minutos para horas e tratamento de campos vazios), gerando o ficheiro `dados_organizados_steam.json`.
3. **Modelagem Inicial e Escopo:** Identificamos as entidades preliminares do banco de dados, definimos os três subtemas possíveis, escolhemos o subtema principal com justificativa (*Storytelling*) e elaboramos as perguntas de negócio que o BD deverá responder.

## 2. Divisão de Responsabilidades
* **[Filipe Tavares]:** Desenvolvimento do script em Python para consumo da API, tratamento dos dados e documentação no GitHub.
* **[Natanael Herculano S. Neto]:** Análise preliminar dos dados, criação do dicionário inicial e identificação de entidades.
* **[Sebastião de Andrade Silva]:** Definição dos subtemas, desenvolvimento do *Storytelling* e elaboração das perguntas para o Banco de Dados.
* **[Gabriel Araújo da Silva]:** Criação da apresentação de slides (Pitch) e revisão geral.

## 3. Relatório Resumido das Reuniões
* **Reunião 01 (09/11/2026):** Conversa para a escolha do tema definidido.
* **Reunião 02 (16/11/2026):** Desenvolvimento e execução do script em Python, análise dos problemas encontrados nos dados brutos e definição das entidades (`Jogo`, `Empresa`, `Desempenho_Comercial`).
* **Reunião 03 (24/11/2026):** Criação do GitHub do projeto, escolha do subtema final, criação das perguntas complexas para o BD e montagem dos slides para o pitch.

  ## 4. Resumo Técnico da Fase 01
### Dicionário Inicial dos Dados
* `appid` (Inteiro): ID único do jogo na Steam.
* `name` (Texto): Nome do jogo.
* `developer` / `publisher` (Texto): Estúdio desenvolvedor e empresa publicadora.
* `positive` / `negative` (Inteiro): Total de avaliações positivas e negativas.
* `average_forever` (Inteiro): Tempo médio jogado em minutos (convertido para horas no ficheiro limpo).
* `price` (Texto/Inteiro): Preço em cêntimos de dólar (convertido para dólares no ficheiro limpo).
* `owners` (Texto): Estimativa da faixa de compradores (ex: `"1,000,000 .. 2,000,000"`).

### Problemas Encontrados nos Dados Brutos
1. **Escala e Tipagem de Preço:** O preço original vem como *string* em cêntimos (exemplo: `"1999"`), exigindo conversão para *float* e divisão por 100. Jogos gratuitos vêm com valor `"0"`.
2. **Intervalo de Compradores em Texto:** O campo `owners` traz intervalos em texto em vez de valores numéricos diretos.
3. **Campos em Branco e Múltiplos Valores:** Alguns registos não possuem `publisher` preenchida ou trazem mais de uma empresa separada por vírgula no mesmo campo.

### Identificação Preliminar de Entidades
* **Jogo:** `(id_jogo, nome, preco_dolares, tempo_medio_horas)`
* **Empresa:** `(id_empresa, nome_empresa, tipo_atuacao)`
* **Desempenho_Comercial:** `(id_desempenho, id_jogo, avaliacoes_positivas, avaliacoes_negativas, faixa_donos)`

### Subtemas e Escolha (Storytelling)
* **Subtemas Elencados:**
  1. Retenção e engajamento de jogadores vs. custo do jogo.
  2. Desempenho de estúdios independentes (autopublicados) vs. grandes *Publishers*.
  3. Impacto do modelo *Free-to-Play* na aprovação da comunidade.
* **Subtema Escolhido:** **Subtema 1.** No mercado de jogos, preços elevados nem sempre garantem maior tempo de jogo ou satisfação. Analisar a correlação entre valor cobrado, horas jogadas e aprovação ajuda jogadores a decidirem melhor as suas compras e estúdios a precificarem os seus jogos de forma justa.

### Perguntas que o Banco de Dados Deverá Responder
1. *Qual a relação entre a faixa de preço do jogo, a taxa de aprovação (proporção entre avaliações positivas e negativas) e o tempo médio de retenção dos jogadores?*
2. *Jogos autopublicados (onde a desenvolvedora é a própria publicadora) conseguem manter uma média de horas jogadas e aprovação superior aos jogos distribuídos por terceiros na mesma faixa de vendas?*
3. *Como o modelo gratuito (preço zero) impacta o volume de rejeição (avaliações negativas) em comparação aos jogos pagos de maior engajamento?*

---
> **Nota sobre uso de IA:** O script de extração e tratamento (`coleta_steam.py`) foi estruturado com o auxílio do Google Gemini. Link público da conversa: [https://share.gemini.google/cyr9j14l0zl2]
