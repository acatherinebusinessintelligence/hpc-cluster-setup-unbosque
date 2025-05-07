import subprocess

def verificar_conectividad(nodo):
    resultado = subprocess.run(["ping", "-c", "3", nodo], capture_output=True, text=True)
    if resultado.returncode == 0:
        print(f" Conectividad exitosa con {nodo}\n{resultado.stdout}")
    else:
        print(f" Fallo de conectividad con {nodo}")
