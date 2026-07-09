# 🤖 Automação de Extração e Tratamento de Relatórios ERP (RPA)

Este repositório contém uma solução de automação robótica de processos (RPA) concebida, modelada e desenvolvida integralmente por mim em **Python**, utilizando **Selenium** e **Pandas**. O objetivo principal do projeto foi eliminar uma tarefa diária, repetitiva e operacional de extração de relatórios de um sistema web corporativo, aplicando filtros de negócios e estruturando o resultado em nuvem.

---

## 📋 O Cenário Antigo (Processo Manual)

Antes do desenvolvimento deste robô, o fluxo operacional exigia que um colaborador realizasse essa tarefa **manualmente todos os dias**, consumindo tempo precioso e abrindo margem para falhas operacionais:

1. **Acesso:** Abrir o navegador e navegar até o sistema interno.
2. **Login:** Inserir manualmente usuário e senha de acesso.
3. **Navegação interna:** Procurar pelo menu de consultas, digitar comandos específicos de pesquisa e navegar até páginas internas profundas do sistema.
4. **Exportação:** Localizar o relatório desejado, configurar os parâmetros de exportação (mudar o formato para CSV, definir o separador por ponto-e-vírgula) e solicitar a geração.
5. **Download:** Aguardar o processamento lento do sistema e salvar o arquivo localmente.
6. **Tratamento:** Abrir o arquivo bruto, rastrear registros e deletar manualmente linhas baseadas em uma regra de negócio específica (remoção de prefixos indesejados).
7. **Backup:** Ir até a pasta de rede, renomear o arquivo antigo com a data do dia para não perder o histórico.
8. **Salvamento Final:** Converter o arquivo para Excel (`.xlsx`), renomear a aba interna e salvar a versão atualizada na pasta compartilhada em nuvem.

---

## ⚡ A Solução Automatizada (Com o Robô)

Com a implementação deste script em Python, **o cenário mudou completamente**. Agora, o usuário apenas executa o robô, que realiza todo o trabalho pesado de forma transparente, ágil e precisa em segundos:

* **Simulação Humana:** O script interage com a interface web simulando o comportamento humano na digitação de credenciais e cliques, reduzindo bloqueios de segurança por robótica.
* **Espera Ativa Inteligente:** Monitora a pasta de downloads do sistema operacional em tempo real. O robô sabe exatamente quando o arquivo terminou de ser baixado (ignorando extensões temporárias como `.crdownload`) e avança de forma dinâmica.
* **Tratamento de Dados em Alta Performance:** Utiliza a biblioteca **Pandas** para processar milhares de linhas instantaneamente, deletando os prefixos configurados e limpando caracteres invisíveis ou ilegais que costumam corromper arquivos do Excel.
* **Gestão de Histórico Automática:** O robô detecta se já existe uma planilha do dia anterior na sua pasta de destino, aplica uma estampa de data e hora (`YYYYMMDD_HHMMSS`) e a move para uma pasta de histórico antes de salvar a nova versão limpa.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

O ecossistema do projeto foi escolhido para garantir leveza, velocidade e facilidade de manutenção:

* **Visual Studio Code (VS Code):** Ambiente de desenvolvimento (IDE) utilizado para a codificação, depuração e versionamento do script.
* **Python 3.x:** Linguagem base de todo o ecossistema.
* **Selenium WebDriver:** Para automação de interface e navegação no navegador (Web Scraping/RPA).
* **Pandas:** Para manipulação analítica rápida do arquivo e aplicação cirúrgica dos filtros de negócio.
* **OpenPyXL:** Engine responsável por gerar o arquivo de saída final perfeitamente formatado e compatível com o Microsoft Excel.

---

## 🚀 Como Configurar e Executar (Guia para Clonar e Rodar)

Se você deseja replicar este projeto na sua máquina ou utilizá-lo como base para a sua própria automação, siga o passo a passo abaixo:

### 1. Pré-requisitos Obrigatórios
Antes de começar, certifique-se de ter instalado em seu computador:
* **Python 3.x** instalado (e marcado a opção "Add Python to PATH" durante a instalação).
* O navegador **Google Chrome** instalado.
* O **Visual Studio Code (VS Code)** ou outra IDE de sua preferência.

### 2. Clonando o Repositório
Abra o terminal do seu computador (ou o terminal integrado do VS Code) e execute o comando abaixo para baixar o projeto:

```bash
git clone [https://github.com/andrereistech/ErgonAuto-RPA.git](https://github.com/andrereistech/ErgonAuto-RPA.git)
```
---

## 🤝 Coautoria e Desenvolvimento

Este projeto foi **idealizado, planejado e direcionado por mim**, que identifiquei o gargalo operacional no dia a dia da empresa e desenhei todo o fluxo da solução. 

Para tirar o projeto do papel com máxima agilidade, utilizei a inteligência artificial **Gemini (Google)** como minha coautora técnica. Eu trouxe as regras de negócio, a lógica do processo e o escopo na cabeça, e o Gemini transformou essa visão em linhas de código Python puras, refinando os filtros do Pandas e estruturando a inteligência de download do robô.

---

## 📫 Conecte-se Comigo

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andre-reis-tech/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/andrereistech)

---
