"""
Script para verificar o status de disponibilidade de uma lista de hosts.

Autor: Elias Andrade
Contato: oeliasandrade@gmail.com
Data: 01/04/2024

Este script utiliza o módulo socket para resolver o endereço IP de uma lista de hosts.
Em seguida, ele verifica se o host está online ou offline e registra o resultado em um arquivo 'hosts_status.txt'.

Funcionalidades:
- Resolve o endereço IP de uma lista de hosts.
- Verifica se os hosts estão online ou offline.
- Registra o status de disponibilidade dos hosts em um arquivo de saída.

Instruções de Uso:
1. Execute o script.
2. Aguarde até que o processo seja concluído.
3. Verifique o arquivo 'hosts_status.txt' para ver o status de disponibilidade dos hosts.

"""

import socket

hosts = [
    "HOSTNAMEEXEMPLO.COM.BR",
]

def resolve_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None

def main():
    with open('hosts_status.txt', 'w') as file:
        for host in hosts:
            ip = resolve_ip(host)
            status = "Online" if ip else "Offline"
            file.write(f"{host} ({ip}): {status}\n")

if __name__ == "__main__":
    main()
