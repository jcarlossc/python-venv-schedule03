# Importa módulos Schedule, Time e Subprocess
import schedule
import time
import subprocess

# Função responsável por executa outro script Python
def executar_script_externo():
    subprocess.run(["python", "scripts_python/meu_script.py"])  

# Agenda a tarefa para ser executar em horário específico
schedule.every().day.at("10:57").do(executar_script_externo)

while True:
    # Executa a tarefa agendada
    schedule.run_pending()

    # Evita sobrecarga da CPU
    time.sleep(1)