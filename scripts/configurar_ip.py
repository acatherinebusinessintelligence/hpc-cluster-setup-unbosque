import subprocess

def configurar_ip(nodo, ip):
    comando = f"ssh {nodo} 'sudo ip addr add {ip}/24 dev eth0 && sudo ip link set eth0 up'"
    subprocess.run(comando, shell=True, check=True)
