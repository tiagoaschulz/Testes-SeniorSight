*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    http://localhost:5173
${BROWSER}     Chrome

*** Test Cases ***
# Página Inicial
Verificar Carregamento Correto da Página Inicial
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    SeniorInsight
    Page Should Contain Element    //header[contains(@class, 'page-header')]
    Page Should Contain Element    //nav[contains(@class, 'bottom-nav')]
    Close Browser

Verificar Exibição do Banner de Alerta
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain Element    //div[contains(@class, 'alert-banner')]
    Close Browser

Verificar Exibição dos Sinais Vitais
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain Element    //div[contains(@class, 'vital-card')]
    Close Browser

Verificar Navegação para Página de Medicações
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Click Link    /medications
    Location Should Be    ${BASE_URL}/medications
    Close Browser

# Página de Medicações
Verificar Carregamento Correto da Página de Medicações
    Open Browser    ${BASE_URL}/medications    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    Medicações
    Page Should Contain Element    //div[contains(@class, 'medication-card')]
    Close Browser

Verificar Busca por um Medicamento
    Open Browser    ${BASE_URL}/medications    ${BROWSER}
    Maximize Browser Window
    Input Text    //input[@placeholder='Buscar']    Paracetamol
    Press Keys    //input[@placeholder='Buscar']    ENTER
    Page Should Contain    Paracetamol
    Close Browser

Verificar Detalhes no Card de Medicamento
    Open Browser    ${BASE_URL}/medications    ${BROWSER}
    Maximize Browser Window
    Click Element    //div[contains(@class, 'medication-card')][1]
    Page Should Contain    Detalhes do Medicamento
    Close Browser

Verificar Navegação para Página de Novo Medicamento
    Open Browser    ${BASE_URL}/medications    ${BROWSER}
    Maximize Browser Window
    Click Link    /medications/new
    Location Should Be    ${BASE_URL}/medications/new
    Close Browser

# Página de Novo Medicamento
Verificar Carregamento Correto da Página de Novo Medicamento
    Open Browser    ${BASE_URL}/medications/new    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    Novo Medicamento
    Page Should Contain Element    //form
    Close Browser

Verificar Adição de Novo Medicamento
    Open Browser    ${BASE_URL}/medications/new    ${BROWSER}
    Maximize Browser Window
    Input Text    //input[@name='name']    Ibuprofeno
    Input Text    //input[@name='dosage']    600mg
    Input Text    //input[@name='time']    12:00
    Click Button    //button[@type='submit']
    Location Should Be    ${BASE_URL}/medications
    Page Should Contain    Ibuprofeno
    Close Browser

Verificar Erro em Submissão de Formulário Inválido
    Open Browser    ${BASE_URL}/medications/new    ${BROWSER}
    Maximize Browser Window
    Click Button    //button[@type='submit']
    Page Should Contain    Por favor, preencha todos os campos.
    Close Browser

Verificar Redirecionamento Após Adicionar Medicamento
    Open Browser    ${BASE_URL}/medications/new    ${BROWSER}
    Maximize Browser Window
    Input Text    //input[@name='name']    Dipirona
    Input Text    //input[@name='dosage']    500mg
    Input Text    //input[@name='time']    08:00
    Click Button    //button[@type='submit']
    Location Should Be    ${BASE_URL}/medications
    Close Browser

# Página de Histórico
Verificar Carregamento Correto da Página de Histórico
    Open Browser    ${BASE_URL}/history    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    Histórico
    Page Should Contain Element    //div[contains(@class, 'timeline-card')]
    Close Browser

Verificar Filtro de Histórico por Data
    Open Browser    ${BASE_URL}/history    ${BROWSER}
    Maximize Browser Window
    Input Text    //input[@type='date']    2024-01-01
    Page Should Contain    01/01/2024
    Close Browser

# Página SOS
Verificar Carregamento Correto da Página SOS
    Open Browser    ${BASE_URL}/sos    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    SOS
    Page Should Contain Element    //section[contains(@class, 'sos-section')]
    Close Browser

Verificar Botão de Chamada SOS
    Open Browser    ${BASE_URL}/sos    ${BROWSER}
    Maximize Browser Window
    Click Button    //button[contains(text(), 'Ligar')]
    # This is a placeholder, as we can't test the call itself
    Page Should Contain    Ligando...
    Close Browser
