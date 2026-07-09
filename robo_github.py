from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pandas as pd
import os
import glob
import shutil

# --- CONFIGURAÇÕES DE CAMINHO (Ajuste para o seu ambiente) ---
CAMINHO_DRIVE = r"C:\Caminho\Para\Seu\Google_Drive\Uploads Relatórios"
NOME_ARQUIVO = "Relatorio_Final.xlsx"
CAMINHO_FINAL = os.path.join(CAMINHO_DRIVE, NOME_ARQUIVO)
PASTA_BACKUP = os.path.join(CAMINHO_DRIVE, "historico_versoes")

# --- CREDENCIAIS DE ACESSO (Mantenha em segredo) ---
USUARIO_SISTEMA = "SEU_USUARIO"
SENHA_SISTEMA = "SUA_SENHA"
URL_SISTEMA = "http://url-do-sistema-da-sua-empresa.com"

def digitar_humano(elemento, texto):
    for caractere in texto:
        elemento.send_keys(caractere)
        time.sleep(random.uniform(0.1, 0.2))

# 1. Inicia o navegador
print("🤖 Iniciando o navegador Chrome...")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL_SISTEMA)
wait = WebDriverWait(driver, 10)

# 2. Login
print("🔐 Inserindo credenciais e realizando login...")
campo_usuario = wait.until(EC.element_to_be_clickable((By.ID, "username")))
campo_usuario.clear()
digitar_humano(campo_usuario, USUARIO_SISTEMA)
time.sleep(1)
campo_senha = driver.find_element(By.ID, "password")
campo_senha.clear()
digitar_humano(campo_senha, SENHA_SISTEMA)
driver.find_element(By.ID, "sendCredentials").click()
print("✅ Login efetuado com sucesso!")

# 3. Executa Consultas
print("🔍 Acessando o menu de consultas...")
time.sleep(3) 
campo_consultas = wait.until(EC.element_to_be_clickable((By.ID, "ext-comp-1002")))
campo_consultas.click()
campo_consultas.send_keys("executa consultas")
time.sleep(1)
campo_consultas.send_keys(Keys.ENTER)

# 4. Navegação de Página
print("📄 Navegando para a página do relatório...")
time.sleep(3) 
campo_numero = wait.until(EC.element_to_be_clickable((By.ID, "ext-comp-1070")))
campo_numero.click()
campo_numero.send_keys(Keys.CONTROL + "a")
campo_numero.send_keys(Keys.BACKSPACE)
campo_numero.send_keys("24") # Altere o número da página se necessário
campo_numero.send_keys(Keys.ENTER)
time.sleep(3)

# 5. Selecionar Relatório
print("📋 Selecionando o relatório alvo...")
item_lista = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'NOME_DO_SEU_RELATORIO')]")))
item_lista.click()
time.sleep(3)

# 6. Alterar para CSV
print("⚙️ Alterando o formato de saída do arquivo para CSV...")
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "drpTipo_arq")))
dropdown.click()
time.sleep(1)
dropdown.send_keys(Keys.CONTROL + "a")
dropdown.send_keys(Keys.BACKSPACE)
dropdown.send_keys("csv")
dropdown.send_keys(Keys.ENTER)
time.sleep(2)

# 7. Preencher separador
campo_separador = driver.find_element(By.ID, "txtSeparador")
campo_separador.clear()
campo_separador.send_keys(";")

# 8. Gerar arquivo
print("📥 Solicitando a geração do arquivo ao sistema...")
botao_gerar = driver.find_element(By.ID, "fldGera_arquivo_2p")
botao_gerar.click()

# 9. Pós-processamento com Espera Ativa do Download
print("⏳ Aguardando o início e conclusão do download na pasta padrão...")

pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
arquivos_antes = set(glob.glob(os.path.join(pasta_downloads, "*.csv")))

arquivo_mais_recente = None
tentativas = 0
max_tentativas = 60 

while tentativas < max_tentativas:
    arquivos_atuais = set(glob.glob(os.path.join(pasta_downloads, "*.csv")))
    novos_arquivos = arquivos_atuais - arquivos_antes
    
    if novos_arquivos:
        possivel_arquivo = max(novos_arquivos, key=os.path.getctime)
        
        if not possivel_arquivo.endswith('.crdownload'):
            arquivo_mais_recente = possivel_arquivo
            print(f"📥 Download concluído! Arquivo identificado: {os.path.basename(arquivo_mais_recente)}")
            break
            
    time.sleep(1)
    tentativas += 1

if not arquivo_mais_recente:
    print("❌ Erro: O download demorou mais de 1 minuto ou falhou.")
    driver.quit()
    exit()

# Leitura e Tratamento
print("📖 Lendo a planilha baixada com o Pandas...")
df = pd.read_csv(arquivo_mais_recente, sep=';', encoding='latin-1', low_memory=False)

print("✂️ Aplicando filtro para exclusão do prefixo específico...")
df = df[df['PREFIXO'].astype(str) != '105']

print("🧼 Limpando caracteres ilegais...")
def limpar_caracteres_ilegais(valor):
    if isinstance(valor, str):
        return "".join(c for c in valor if ord(c) >= 32 or c in "\n\r\t")
    return valor

df = df.map(limpar_caracteres_ilegais)

# Garante que as pastas de destino existam
if not os.path.exists(CAMINHO_DRIVE):
    os.makedirs(CAMINHO_DRIVE)
if not os.path.exists(PASTA_BACKUP):
    os.makedirs(PASTA_BACKUP)

# Cria o Backup Histórico da versão antiga se ela já existir
if os.path.exists(CAMINHO_FINAL):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    print(f"📦 Gerando cópia de backup da versão anterior na pasta histórica...")
    shutil.move(CAMINHO_FINAL, os.path.join(PASTA_BACKUP, f"Relatorio_Final_{timestamp}.xlsx"))

# Salvar novo arquivo tratado no Drive
print(f"💾 Salvando o novo arquivo e definindo o nome da aba na sua pasta de destino...")
with pd.ExcelWriter(CAMINHO_FINAL, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='DADOS_TRATADOS', index=False)

print(f"🏁 Processo concluído com sucesso!")

driver.quit()
