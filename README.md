# CPFL Energy Analytics ⚡

Projeto de estudo em **Python, SQL e visualização de dados** focado na **análise de interrupções de energia** e seus impactos operacionais.

Este repositório foi estruturado para simular um cenário real de trabalho em uma área de **Data Analytics / Operação de Distribuidora de Energia**, com foco em:

- Entender **onde** e **por que** ocorrem mais interrupções  
- Avaliar o **impacto nos clientes**  
- Medir a **duração média** das ocorrências  
- Gerar **gráficos e insights** que apoiem a decisão operacional  

> ⚠️ **Observação:** Os dados utilizados são fictícios, criados apenas para fins de estudo, sem qualquer vínculo com dados reais da CPFL.

---

## 🎯 Objetivos do Projeto

- Praticar **análise de dados** com foco em operação de energia elétrica  
- Construir uma base tratada a partir de dados brutos (`raw` → `processed`)  
- Criar **notebooks explicativos** com análise exploratória e dashboard operacional  
- Mostrar habilidades alinhadas a uma vaga de **Analista de Data Analytics**

---

## 🧱 Estrutura do Projeto

```bash
cpfl-energy-analytics/
├── data/
│   ├── raw/
│   │   └── interrupcoes_raw.csv        # Dados brutos das interrupções
│   └── processed/
│       └── interrupcoes_clean.csv     # Dados tratados e prontos para análise
│
├── notebooks/
│   ├── 01_exploracao_interrupcoes.ipynb      # Análise exploratória (EDA)
│   └── 02_dashboard_operacional.ipynb        # Dashboard operacional em gráficos
│
├── src/
│   └── analise_interrupcoes.py        # Script principal de tratamento dos dados
│
├── .venv/                             # Ambiente virtual (ignorado no Git)
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Tecnologias Utilizadas

Python 3.9

Pandas

Matplotlib

Jupyter Notebook

Git & GitHub

Ambiente virtual (venv)

🚀 Como Executar o Projeto Localmente

1. Clonar o repositório

git clone https://github.com/BrunoApMarques/cpfl-energy-analytics.git
cd cpfl-energy-analytics

2. Criar e ativar o ambiente virtual (Windows – Git Bash)

python -m venv .venv
source .venv/Scripts/activate

3. Instalar as dependências

pip install -r requirements.txt

4. Gerar o dataset tratado

python src/analise_interrupcoes.py

Esse script faz:

Leitura do arquivo bruto (raw)

Conversão de datas

Cálculo da duração das ocorrências

Geração do arquivo limpo em processed/

5. Executar os notebooks

Abra:

01_exploracao_interrupcoes.ipynb

02_dashboard_operacional.ipynb

Selecione o Kernel do .venv antes de rodar.

📊 Análises Realizadas
📌 1. Ocorrências por Região

Identifica regiões com maior frequência de interrupções.
Ajuda na priorização operacional.

📌 2. Ocorrências por Causa da Interrupção

Mostra quais fatores mais impactam a rede:

Temporal

Equipamento

Acidente

Manutenção

📌 3. Total de Clientes Afetados por Região

Quantifica o impacto real na população.
Regiões são comparadas pelo total de clientes atingidos.

📌 4. Duração Média das Ocorrências

Indicadores calculados:

Duração média por região

Duração média por causa

Duração média por status (Concluída / Em atendimento)

Esses dados são essenciais para medir eficiência operacional.


🧠 Resumo Executivo (Insights)

A análise revela:

Indaiatuba e Campinas foram as regiões com maior número de ocorrências.

As maiores durações médias estão associadas a Acidentes e Temporais.

A soma de clientes afetados indica forte impacto em alguns municípios.

A análise por status evidencia diferença de tratamento entre ocorrências concluídas e em andamento.

Essas informações são típicas de análises feitas em:

Centros de Operação (COI)

Times de Data Analytics

Planejamento Operacional

Melhorias de rede


Este projeto demonstra habilidades práticas diretamente relacionadas ao dia a dia da função:

✔ Tratamento e limpeza de dados
✔ Construção de indicadores operacionais
✔ Conhecimento em Pandas e Python
✔ Análises exploratórias profissionais
✔ Criação de gráficos e dashboards
✔ Estruturação organizada em GitHub

