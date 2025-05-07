from configurar_ip import configurar_ip
from configurar_hostname import configurar_hostname
from verificar_conectividad import verificar_conectividad
from instalar_paquetes import instalar_paquetes

nodo = "192.168.56.101"
ip = "192.168.56.101"
hostname = "nodo1"
paquetes = ["gcc", "openmpi"]

configurar_ip(nodo, ip)
configurar_hostname(nodo, hostname)
verificar_conectividad(nodo)
instalar_paquetes(nodo, paquetes)
