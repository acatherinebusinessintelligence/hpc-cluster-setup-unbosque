# 🧪 Guía Paso a Paso para la Ejecución del Proyecto HPC

## 📌 Objetivo
Ejecutar los scripts de configuración de red, hostname, conectividad e instalación de software sobre nodos de un clúster HPC simulado o real, utilizando Python y SSH.

---

## 🔧 Requisitos Previos

| Elemento                     | Requisito                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| Sistema Operativo           | Ubuntu Server o cualquier distribución Linux                             |
| Acceso entre nodos          | SSH habilitado y autenticación con claves (`ssh-keygen` + `ssh-copy-id`) |
| Python                      | Python 3 instalado (`python3 --version`)                                  |
| Permisos                    | Usuario con permisos sudo                                                 |
| Red                         | IPs estáticas asignadas y conectividad en la misma red LAN o NAT         |

---

## 📁 Estructura del Proyecto Esperada

```
hpc-cluster-setup-unbosque/
├── scripts/
│   ├── configurar_ip.py
│   ├── configurar_hostname.py
│   ├── verificar_conectividad.py
│   └── instalar_paquetes.py
├── docs/
│   └── bitacora_instalacion.md
├── README.md
├── LICENSE
└── main.py (opcional)
```

---

## 🚀 Ejecución Paso a Paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/hpc-cluster-setup-unbosque.git
cd hpc-cluster-setup-unbosque/scripts
```

### 2. Configurar IP del nodo remoto

Editar el archivo `configurar_ip.py` o agregar esta línea temporalmente al final:

```python
configurar_ip("192.168.56.101", "192.168.56.101")
```

Luego ejecutar:

```bash
python3 configurar_ip.py
```

---

### 3. Configurar el nombre del host

Editar `configurar_hostname.py` con:

```python
configurar_hostname("192.168.56.101", "nodo1")
```

Y ejecutar:

```bash
python3 configurar_hostname.py
```

---

### 4. Verificar conectividad

```bash
python3 verificar_conectividad.py
```

---

### 5. Instalar paquetes necesarios

Editar `instalar_paquetes.py` y agregar:

```python
instalar_paquetes("192.168.56.101", ["gcc", "openmpi"])
```

Ejecutar:

```bash
python3 instalar_paquetes.py
```

---

## 🧠 Alternativa: Ejecutar todo desde un solo archivo `main.py`

### Crear `main.py` en la raíz:

```python
from scripts.configurar_ip import configurar_ip
from scripts.configurar_hostname import configurar_hostname
from scripts.verificar_conectividad import verificar_conectividad
from scripts.instalar_paquetes import instalar_paquetes

nodo = "192.168.56.101"
ip = "192.168.56.101"
hostname = "nodo1"
paquetes = ["gcc", "openmpi"]

configurar_ip(nodo, ip)
configurar_hostname(nodo, hostname)
verificar_conectividad(nodo)
instalar_paquetes(nodo, paquetes)
```

### Ejecutar:

```bash
python3 main.py
```

---

## ✅ Resultado Esperado

- El nodo tendrá IP fija configurada.
- El hostname será visible al ejecutar `hostname`.
- Ping funcional entre nodos.
- Paquetes instalados para computación distribuida (OpenMPI, GCC, etc.).
