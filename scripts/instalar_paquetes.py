import subprocess

def instalar_paquetes(nodo, lista_paquetes):
    paquetes = " ".join(lista_paquetes)
    comando = f"ssh {nodo} 'sudo apt install -y {paquetes}'"
    subprocess.run(comando, shell=True, check=True)
