###########################################################################
# Arquivo: manual_hardening_linux_ubuntu.txt                              #
# Descrição: Manual de Hardening para o Linux Ubuntu 22.                  #
# Criado por: Elias Andrade - Analista DevOps                             #
# LinkedIn: https://www.linkedin.com/in/elias-andrade-21574b2b4/          #
# Data: 15/02/2024                                                        #
###########################################################################

# Manual de Hardening para Linux Ubuntu 22:

## 1. Atualização do Sistema:

### - Manter o sistema sempre atualizado:
sudo apt update
sudo apt upgrade

## 2. Configuração de Usuários:

### - Criar usuários com privilégios mínimos:
sudo adduser novo_usuario

### - Remover acesso de superusuário de usuários desnecessários:
sudo deluser usuario_desnecessario sudo

## 3. Configuração do Firewall (UFW):

### - Instalar o UFW (Uncomplicated Firewall):
sudo apt install ufw

### - Habilitar o UFW:
sudo ufw enable

### - Definir uma política padrão para negar tráfego de entrada:
sudo ufw default deny incoming

### - Definir uma política padrão para permitir tráfego de saída:
sudo ufw default allow outgoing

### - Permitir tráfego SSH:
sudo ufw allow ssh

### - Permitir tráfego HTTP:
sudo ufw allow http

### - Permitir tráfego HTTPS:
sudo ufw allow https

### - Verificar o status do UFW:
sudo ufw status verbose

## 4. Configuração de Segurança do Kernel:

### - Atualizar o kernel para a versão mais recente:
sudo apt install linux-generic

### - Configurar parâmetros de segurança do kernel no sysctl.conf:
sudo nano /etc/sysctl.conf

# Adicionar as seguintes linhas no final do arquivo:
# Proteger contra spoofing de IP:
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Proteger contra SYN flood attacks:
net.ipv4.tcp_syncookies = 1

# Desabilitar o redirecionamento de pacotes:
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0

# Proteger contra o ataque de ping da morte:
net.ipv4.icmp_echo_ignore_broadcasts = 1

# Desabilitar respostas de eco ICMP:
net.ipv4.icmp_echo_ignore_all = 1

# Aplicar as configurações:
sudo sysctl -p

## 5. Configuração de Acesso Remoto:

### - Restringir acesso remoto apenas a IPs confiáveis:
sudo nano /etc/hosts.allow

# Adicionar as seguintes linhas:
sshd: IP_confiavel

sudo nano /etc/hosts.deny

# Adicionar a seguinte linha:
sshd: ALL

### - Desabilitar login de root via SSH:
sudo nano /etc/ssh/sshd_config

# Alterar PermitRootLogin para no:
PermitRootLogin no

# Reiniciar o serviço SSH:
sudo systemctl restart ssh

## 6. Monitoramento de Logs:

### - Configurar o rsyslog para enviar logs para um servidor remoto:
sudo nano /etc/rsyslog.conf

# Descomentar a linha abaixo e substituir "IP_servidor_remoto" pelo endereço do servidor remoto:
#*.* @IP_servidor_remoto:514

# Reiniciar o serviço rsyslog:
sudo systemctl restart rsyslog

## 7. Auditar Logs de Autenticação:

### - Instalar e configurar o auditd:
sudo apt install auditd

### - Configurar regras de auditoria para monitorar arquivos de autenticação:
sudo nano /etc/audit/rules.d/audit.rules

# Adicionar as seguintes linhas:
-w /var/log/auth.log -p wa -k authentication_log

# Reiniciar o serviço auditd:
sudo systemctl restart auditd

## 8. Configuração de Firewall de Aplicativo (APPArmor):

### - Instalar o APPArmor:
sudo apt install apparmor

### - Ativar o APPArmor:
sudo aa-enforce /etc/apparmor.d/*

### - Verificar o status do APPArmor:
sudo aa-status

## 9. Monitoramento de Integridade de Arquivos:

### - Instalar o AIDE (Advanced Intrusion Detection Environment):
sudo apt install aide

### - Inicializar o banco de dados do AIDE:
sudo aideinit

### - Verificar a integridade dos arquivos:
sudo aide --check

## 10. Configuração de Política de Senhas:

### - Configurar a política de senhas no arquivo /etc/login.defs
sudo nano /etc/login.defs

# Alterar os seguintes parâmetros conforme necessário:
PASS_MAX_DAYS   90
PASS_MIN_DAYS   7
PASS_WARN_AGE   7

### - Forçar senhas seguras com o PAM:
sudo apt install libpam-cracklib

### - Editar a configuração do PAM:
sudo nano /etc/pam.d/common-password

# Adicionar a seguinte linha no final do bloco:
password requisite pam_cracklib.so retry=3 minlen=12 difok=3

## 11. Configuração de Política de Bloqueio de Conta:

### - Configurar a política de bloqueio de conta no PAM:
sudo nano /etc/pam.d/common-auth

# Adicionar a seguinte linha no final do bloco:
auth required pam_tally2.so deny=3 unlock_time=600 onerr=fail

### - Configurar o tempo de bloqueio de conta:
sudo pam_tally2 --deny=3 --lock-time=600

### - Resetar contadores de tentativas de login:
sudo pam_tally2 --reset

## 12. Configuração de Segurança de Rede:

### - Habilitar filtragem de pacotes no kernel:
sudo nano /etc/ufw/sysctl.conf

# Adicionar as seguintes linhas:
net.ipv4.ip_forward=0
net.ipv4.conf.all.send_redirects=0
net.ipv4.conf.default.send_redirects=0
net.ipv4.conf.all.accept_source_route=0
net.ipv4.conf.default.accept_source_route=0
net.ipv4.conf.all.accept_redirects=0
net.ipv4.conf.default.accept_redirects=0
net.ipv4.conf.all.secure_redirects=0
net.ipv4.conf.default.secure_redirects=0
net.ipv4.conf.all.log_martians=1
net.ipv4.conf.default.log_martians=1

# Reiniciar o serviço UFW:
sudo systemctl restart ufw

## 13. Desabilitar Serviços Desnecessários:

### - Listar serviços em execução:
sudo systemctl list-unit-files --state=enabled

### - Desabilitar serviços desnecessários:
sudo systemctl disable nome_servico

## 14. Monitoramento de Integridade do Sistema:

### - Configurar e instalar o Tripwire:
sudo apt install tripwire

### - Inicializar a configuração do Tripwire:
sudo tripwire --init

### - Atualizar a base de dados do Tripwire:
sudo tripwire --update

### - Verificar a integridade do sistema com o Tripwire:
sudo tripwire --check

## 15. Criptografia de Disco:

### - Criptografar o disco com o LUKS:
sudo apt install cryptsetup
sudo cryptsetup luksFormat /dev/sdaX
sudo cryptsetup luksOpen /dev/sdaX nome_dispositivo
sudo mkfs.ext4 /dev/mapper/nome_dispositivo
sudo mount /dev/mapper/nome_dispositivo /mnt

## 16. Remover Pacotes Desnecessários:

### - Remover pacotes desnecessários e vulneráveis:
sudo apt autoremove
sudo apt purge nome_pacote

## 17. Configuração de Grupos de Usuários:

### - Criar grupos de usuários para gerenciar permissões:
sudo addgroup nome_grupo

### - Atribuir usuários aos grupos:
sudo adduser nome_usuario nome_grupo

## 18. Monitoramento de Integridade de Arquivo:

### - Instalar o OSSEC (Open Source Security):
sudo apt install ossec-hids-server

### - Configurar o OSSEC:
sudo /var/ossec/bin/manage_agents
