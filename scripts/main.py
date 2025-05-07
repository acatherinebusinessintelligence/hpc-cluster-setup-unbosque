from scripts.configurar_ip import configurar_ip
from scripts.configurar_hostname import configurar_hostname
from scripts.verificar_conectividad import verificar_conectividad
from scripts.instalar_paquetes import instalar_paquetes

# Parámetros de configuración
nodo = "192.168.56.101"
ip = "192.168.56.101"
hostname = "nodo1"
paquetes = ["gcc", "openmpi"]

# Ejecución de scripts
print("🔧 Configurando IP...")
configurar_ip(nodo, ip)

print("🖥️ Configurando hostname...")
configurar_hostname(nodo, hostname)

print("🌐 Verificando conectividad...")
verificar_conectividad(nodo)

print("📦 Instalando paquetes...")
instalar_paquetes(nodo, paquetes)

print("✅ Configuración completada exitosamente.")
