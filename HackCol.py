"Importación de librerías"
import requests
import json


# Función para obtener la región de una IP desde un dominio
def obtenerIpDesdeDominio(dominio):
    """
    Obtiene la dirección IP asociada a un dominio y la región geográfica de la IP.

    Parámetros:
    dominio (str): El dominio del que se desea obtener la información de IP.
    """
    print(f"------------ Dominio -> {dominio} ------------")

    # Solicitud a la API de NetworkCalc para obtener registros DNS
    resultadoBusqueda = requests.get(f"https://networkcalc.com/api/dns/lookup/{dominio}")
    data = resultadoBusqueda.json()

    # Verificar si hay registros de tipo 'A' en la respuesta
    if 'records' in data and data['records'] and 'A' in data['records']:
        for registro in data['records']['A']:
            ip = registro['address']

            # Solicitud a la API de IPinfo para obtener información de la IP
            resultadoRegion = requests.get(f"https://ipinfo.io/{ip}/json")
            region = resultadoRegion.json().get('region', 'Desconocida')

            # Imprimir la región de la IP
            print(f"La región de la IP -> {ip} es {region}")


# Función para obtener correos electrónicos desde un dominio
def obtenerEmailsDesdeDominio(dominio):
    """
    Obtiene una lista de correos electrónicos asociados con un dominio usando la API de Hunter.

    Parámetros:
    dominio (str): El dominio del que se desea obtener la lista de correos electrónicos.
    """
    api_key = 'tu_clave_api_aqui'  # Reemplaza con tu clave API de Hunter
    resultadoEmails = requests.get(f"https://api.hunter.io/v2/domain-search?domain={dominio}&api_key={api_key}")
    data = resultadoEmails.json().get('data', {})

    emails = data.get('emails', [])

    # Imprimir los correos electrónicos en formato JSON
    print(json.dumps(emails, indent=4))

    # Imprimir cada correo electrónico individualmente
    for correo in emails:
        print(f"Correo: {correo['value']}")


# Lista de dominios de empresas para obtener información de IP
dominios_empresas = [
    "atiempo.co",
    "bancolombia.com",
    "banorte.com",
    "exito.com",
    "suramericana.com",
    "cemexcolombia.com",
    "grupobavaria.com",
    "homecenter.co",
    "alfalaval.com",
    "grupocarvajal.com",
    "tdcolombia.com",
    "cerveceriabavaria.com",
    "une.com.co",
    "vanti.com.co",
    "isa.co",
    "sanitas.com.co",
    "corpgroup.com.co",
    "pacificrubiales.com",
    "postobon.com",
    "queretaro.com.co",
    "davivienda.com",
    "fenalco.com.co",
    "epm.com.co",
    "grupohachette.com",
    "jg.com.co",
    "interrapidisimo.com",
    "prosegur.com.co",
    "gsc.co",
    "nexos.com.co",
    "servientrega.com"
]

# Descomentar para usar con la lista de dominios
# for dominio in dominios_empresas:
#     obtenerIpDesdeDominio(dominio)

# Ejemplo de llamada para obtener correos electrónicos
obtenerEmailsDesdeDominio("dersa.com.co")
