import subprocess

def configurar_hostname(nodo, nombre_host):
    comando = f"ssh {nodo} 'sudo hostnamectl set-hostname {nombre_host} && echo \"127.0.0.1 {nombre_host}\" | sudo tee -a /etc/hosts'"
    subprocess.run(comando, shell=True, check=True)
