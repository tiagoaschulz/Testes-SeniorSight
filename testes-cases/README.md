# Testes Automatizados de Interface - SeniorInsight

Este diretório contém os casos de teste automatizados para a interface web do projeto SeniorInsight, utilizando Robot Framework e Selenium.

## Visão Geral

Os testes foram projetados para simular a interação de um usuário com a aplicação, validando as principais funcionalidades, como navegação, visualização de dados e preenchimento de formulários.

## Pré-requisitos

Antes de executar os testes, certifique-se de que você tem o seguinte ambiente configurado:

1.  **Python:** [Instale o Python](https://www.python.org/downloads/) (versão 3.6 ou superior).
2.  **pip:** O gerenciador de pacotes do Python (geralmente vem com a instalação do Python).
3.  **Bibliotecas do Robot Framework:** Instale as bibliotecas necessárias com o seguinte comando:
    ```bash
    pip install robotframework robotframework-seleniumlibrary
    ```
4.  **WebDriver:** Você precisa do driver correspondente ao navegador que deseja usar. Os testes estão configurados para o Chrome.
    *   [Baixe o ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) compatível com a sua versão do Google Chrome.
    *   **Importante:** Adicione o diretório onde você salvou o `chromedriver.exe` à variável de ambiente `PATH` do seu sistema.

## Como Executar os Testes

1.  Navegue até o diretório `testes-cases` pelo terminal.
2.  Execute o seguinte comando:

    ```bash
    robot test_cases.robot
    ```

O Robot Framework irá executar todos os cenários de teste definidos no arquivo `test_cases.robot` e gerará um relatório detalhado (`report.html`) e um log (`log.html`) no mesmo diretório.

## Cenários de Teste

Aqui está uma descrição de cada cenário de teste implementado:

### Página Inicial (Home)

1.  **Verify Home Page Loads Correctly:**
    *   **O que testa:** Verifica se a página inicial é carregada corretamente.
    *   **Como:** Abre a URL base, maximiza a janela e confirma se o título "SeniorInsight", o cabeçalho e a barra de navegação inferior estão presentes.

2.  **Verify Alert Banner is Displayed:**
    *   **O que testa:** Garante que o banner de alerta, uma funcionalidade importante da home, é exibido.
    *   **Como:** Carrega a página e procura pelo elemento do banner de alerta.

3.  **Verify Vital Signs are Displayed:**
    *   **O que testa:** Confirma se os cards com os sinais vitais do paciente são exibidos.
    *   **Como:** Carrega a página e verifica a existência de pelo menos um card de sinal vital.

4.  **Verify Navigation to Medications Page:**
    *   **O que testa:** Valida a navegação da home para a página de medicamentos.
    *   **Como:** Clica no link de navegação para "/medications" e confirma se a URL mudou para a página de medicamentos.

### Página de Medicações

5.  **Verify Medications Page Loads Correctly:**
    *   **O que testa:** Verifica se a página de listagem de medicamentos carrega corretamente.
    *   **Como:** Acessa a URL `/medications` e verifica se o título "Medicações" e pelo menos um card de medicamento estão visíveis.

6.  **Verify Search for a Medication:**
    *   **O que testa:** Testa a funcionalidade de busca de medicamentos.
    *   **Como:** Digita "Paracetamol" no campo de busca, pressiona Enter e verifica se o medicamento "Paracetamol" aparece na lista.

7.  **Verify Medication Card Details:**
    *   **O que testa:** Simula o clique em um medicamento para ver seus detalhes (funcionalidade a ser implementada).
    *   **Como:** Clica no primeiro card de medicamento e espera que a página contenha o texto "Detalhes do Medicamento".

8.  **Verify Navigation to New Medication Page:**
    *   **O que testa:** Valida a navegação para a página de cadastro de novo medicamento.
    *   **Como:** Clica no link para "/medications/new" e confirma se a URL foi alterada corretamente.

### Página de Novo Medicamento

9.  **Verify New Medication Page Loads Correctly:**
    *   **O que testa:** Garante que a página de formulário para adicionar um novo medicamento é carregada.
    *   **Como:** Acessa a URL `/medications/new` e verifica a presença do título "Novo Medicamento" e de um elemento de formulário.

10. **Verify Add New Medication:**
    *   **O que testa:** Testa o fluxo completo de adicionar um novo medicamento.
    *   **Como:** Preenche os campos de nome, dosagem e horário, submete o formulário e verifica se foi redirecionado para a página de medicamentos, onde o novo item deve estar listado.

11. **Verify Error on Invalid Form Submission:**
    *   **O que testa:** Valida se o sistema exibe uma mensagem de erro ao tentar submeter o formulário em branco.
    *   **Como:** Clica no botão de submissão sem preencher os campos e verifica se a mensagem de erro "Por favor, preencha todos os campos." é exibida.

12. **Verify Redirect After Adding Medication:**
    *   **O que testa:** Confirma o redirecionamento após o cadastro bem-sucedido.
    *   **Como:** Preenche o formulário, submete e verifica se a URL final é a da página de listagem de medicamentos.

### Página de Histórico

13. **Verify History Page Loads Correctly:**
    *   **O que testa:** Verifica o carregamento da página de histórico.
    *   **Como:** Acessa a URL `/history` e confirma a presença do título "Histórico" e de um card de evento na linha do tempo.

14. **Verify Filter History by Date:**
    *   **O que testa:** Testa a funcionalidade de filtro por data (funcionalidade a ser implementada).
    *   **Como:** Insere uma data no campo de filtro e verifica se a data correspondente aparece nos resultados.

### Página SOS

15. **Verify SOS Page Loads Correctly:**
    *   **O que testa:** Garante que a página de emergência (SOS) é carregada.
    *   **Como:** Acessa a URL `/sos` e verifica a presença do título "SOS" e de um contato de emergência.

16. **Verify SOS Call Button:**
    *   **O que testa:** Simula o clique no botão de chamada de emergência.
    *   **Como:** Clica no botão "Ligar" e verifica se uma mensagem de status (ex: "Ligando...") é exibida. Este teste não pode validar a chamada real.
