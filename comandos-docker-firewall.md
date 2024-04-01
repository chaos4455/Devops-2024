###########################################################################
# Arquivo: configuracao_firewall_ubuntu.txt                               #
# Descrição: Lista de comandos e funções para configurar o firewall no    #
# ambiente Ubuntu usando UFW.                                             #
# Criado por: Elias Andrade - Analista DevOps                             #
# LinkedIn: https://www.linkedin.com/in/elias-andrade-21574b2b4/          #
# Data: 15/02/2024                                                        #
###########################################################################

# Comandos e Funções para Configuração do Firewall no Ubuntu com UFW:

# 1. Instalar o UFW:
sudo apt update
sudo apt install ufw

# 2. Habilitar o UFW:
sudo ufw enable

# 3. Desabilitar o UFW:
sudo ufw disable

# 4. Exibir o status do UFW:
sudo ufw status

# 5. Permitir tráfego SSH:
sudo ufw allow ssh

# 6. Permitir tráfego HTTP:
sudo ufw allow http

# 7. Permitir tráfego HTTPS:
sudo ufw allow https

# 8. Permitir tráfego em uma porta específica:
sudo ufw allow 8080

# 9. Negar tráfego em uma porta específica:
sudo ufw deny 22

# 10. Permitir tráfego de uma faixa de IPs:
sudo ufw allow from 192.168.1.0/24

# 11. Negar tráfego de uma faixa de IPs:
sudo ufw deny from 10.0.0.0/8

# 12. Permitir tráfego de uma interface específica:
sudo ufw allow in on eth0

# 13. Permitir tráfego para um IP específico e porta:
sudo ufw allow from 203.0.113.5 to any port 3306

# 14. Permitir tráfego para um IP e porta específicos:
sudo ufw allow from 203.0.113.5 to any port 22

# 15. Permitir tráfego para uma rede específica e porta:
sudo ufw allow from 192.168.1.0/24 to any port 80

# 16. Permitir tráfego para um intervalo de portas:
sudo ufw allow 8000:9000/tcp

# 17. Permitir tráfego para um protocolo específico:
sudo ufw allow proto tcp from any to any port 22

# 18. Permitir tráfego para uma porta específica em um protocolo específico:
sudo ufw allow proto tcp from any to any port 80

# 19. Permitir tráfego para uma porta específica em uma faixa de IPs específica:
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp

# 20. Negar tráfego para uma porta específica em um protocolo específico:
sudo ufw deny proto tcp to any port 22

# 21. Permitir tráfego de uma interface específica para uma porta específica:
sudo ufw allow in on eth0 to any port 22

# 22. Permitir tráfego de uma interface específica para uma faixa de IPs específica:
sudo ufw allow in on eth0 from 192.168.1.0/24

# 23. Negar tráfego de uma interface específica para uma porta específica:
sudo ufw deny in on eth0 to any port 22

# 24. Negar tráfego de uma interface específica para uma faixa de IPs específica:
sudo ufw deny in on eth0 from 192.168.1.0/24

# 25. Definir uma regra padrão para permitir tráfego:
sudo ufw default allow

# 26. Definir uma regra padrão para negar tráfego:
sudo ufw default deny

# 27. Permitir tráfego de saída para um IP específico e porta:
sudo ufw allow out to 203.0.113.5 port 3306

# 28. Permitir tráfego de saída para uma interface específica:
sudo ufw allow out on eth0

# 29. Permitir tráfego de saída para uma porta específica em um protocolo específico:
sudo ufw allow out to any port 80 proto tcp

# 30. Negar tráfego de saída para uma porta específica:
sudo ufw deny out to any port 22

# 31. Negar tráfego de saída para uma interface específica:
sudo ufw deny out on eth0

# 32. Permitir tráfego de saída para uma faixa de IPs específica:
sudo ufw allow out to 192.168.1.0/24

# 33. Negar tráfego de saída para uma faixa de IPs específica:
sudo ufw deny out to 192.168.1.0/24

# 34. Permitir tráfego de saída para um protocolo específico:
sudo ufw allow out proto tcp

# 35. Negar tráfego de saída para um protocolo específico:
sudo ufw deny out proto udp

# 36. Permitir tráfego de saída para uma faixa de portas:
sudo ufw allow out 8000:9000/tcp

# 37. Negar tráfego de saída para uma faixa de portas:
sudo ufw deny out 8080:8090/tcp

# 38. Definir uma regra padrão para permitir tráfego de saída:
sudo ufw default allow outgoing

# 39. Definir uma regra padrão para negar tráfego de saída:
sudo ufw default deny outgoing

# 40. Permitir ou negar tráfego de entrada para uma aplicação específica:
sudo ufw allow OpenSSH

# 41. Permitir ou negar tráfego de saída para uma aplicação específica:
sudo ufw allow out OpenSSH

# 42. Permitir tráfego para uma porta específica em uma faixa de IPs específica em uma interface específica:
sudo ufw allow in on eth0 from 192.168.1.0/24 to any port 22

# 43. Negar tráfego para uma porta específica em uma faixa de IPs específica em uma interface específica:
sudo ufw deny in on eth0 from 192.168.1.0/24 to any port 22

# 44. Permitir tráfego de saída para uma porta específica em uma faixa de IPs específica em uma interface específica:
sudo ufw allow out on eth0 from any to 192.168.1.0/24 port 80

# 45. Negar tráfego de saída para uma porta específica em uma faixa de IPs específica em uma interface específica:
sudo ufw deny out on eth0 from any to 192.168.1.0/24 port 22

# 46. Limpar todas as regras e definir as políticas padrão:
sudo ufw reset

# 47. Listar todas as regras:
sudo ufw show raw

# 48. Listar todas as regras com informações detalhadas:
sudo ufw show numbered

# 49. Listar todas as regras aplicadas em um formato mais legível:
sudo ufw status verbose

# 50. Listar todas as regras com as portas resolvidas para os serviços correspondentes:
sudo ufw app list

# 51. Habilitar uma aplicação específica:
sudo ufw allow 'Apache'

# 52. Desabilitar uma aplicação específica:
sudo ufw delete allow 'Apache'

# 53. Habilitar tráfego para um aplicativo personalizado em uma porta personalizada:
sudo ufw allow 1234/tcp

# 54. Desabilitar tráfego para um aplicativo personalizado em uma porta personalizada:
sudo ufw delete allow 1234/tcp

# 55. Habilitar tráfego para um aplicativo personalizado em uma porta personalizada e protocolo:
sudo ufw allow proto tcp from any to any port 1234

# 56. Desabilitar tráfego para um aplicativo personalizado em uma porta personalizada e protocolo:
sudo ufw delete allow proto tcp from any to any port 1234

# 57. Habilitar log para todas as conexões bloqueadas:
sudo ufw logging on

# 58. Desabilitar log para todas as conexões bloqueadas:
sudo ufw logging off

# 59. Configurar log para registrar em um arquivo específico:
sudo ufw logging on /var/log/ufw.log

# 60. Limpar o log atual:
sudo ufw logging off
sudo touch /var/log/ufw.log
sudo chown syslog:adm /var/log/ufw.log
sudo chmod 640 /var/log/ufw.log

# 61. Habilitar regras de configuração de rede IPv6:
sudo ufw ipv6 enable

# 62. Desabilitar regras de configuração de rede IPv6:
sudo ufw ipv6 disable

# 63. Permitir tráfego em uma porta específica para IPv6:
sudo ufw allow 22/tcp6

# 64. Negar tráfego em uma porta específica para IPv6:
sudo ufw deny 25/tcp6

# 65. Permitir tráfego de uma faixa de IPs específica para IPv6:
sudo ufw allow from 2001:db8::/32

# 66. Negar tráfego de uma faixa de IPs específica para IPv6:
sudo ufw deny from 2001:db8::/32

# 67. Permitir tráfego para um IP específico e porta para IPv6:
sudo ufw allow from 2001:db8::1 to any port 80

# 68. Negar tráfego para um IP específico e porta para IPv6:
sudo ufw deny from 2001:db8::1 to any port 443

# 69. Habilitar tráfego para uma faixa de portas para IPv6:
sudo ufw allow 8000:9000/tcp6

# 70. Desabilitar tráfego para uma faixa de portas para IPv6:
sudo ufw deny 8080:8090/tcp6

# 71. Definir uma regra padrão para permitir tráfego para IPv6:
sudo ufw default allow ipv6

# 72. Definir uma regra padrão para negar tráfego para IPv6:
sudo ufw default deny ipv6

# 73. Permitir tráfego de saída para uma porta específica para IPv6:
sudo ufw allow out 1234/udp6

# 74. Negar tráfego de saída para uma porta específica para IPv6:
sudo ufw deny out 5678/tcp6

# 75. Permitir tráfego de saída para uma faixa de portas para IPv6:
sudo ufw allow out 8000:9000/tcp6

# 76. Negar tráfego de saída para uma faixa de portas para IPv6:
sudo ufw deny out 8080:8090/tcp6

# 77. Permitir tráfego de saída para um IP específico e porta para IPv6:
sudo ufw allow out to 2001:db8::1 port 80

# 78. Negar tráfego de saída para um IP específico e porta para IPv6:
sudo ufw deny out to 2001:db8::1 port 443

# 79. Limpar todas as regras IPv6 e definir as políticas padrão:
sudo ufw reset

# 80. Listar todas as regras IPv6:
sudo ufw show raw

# 81. Listar todas as regras IPv6 com informações detalhadas:
sudo ufw show numbered

# 82. Listar todas as regras IPv6 aplicadas em um formato mais legível:
sudo ufw status verbose

# 83. Listar todas as regras IPv6 com as portas resolvidas para os serviços correspondentes:
sudo ufw app list

# 84. Habilitar uma aplicação específica para IPv6:
sudo ufw allow 'Nginx Full'

# 85. Desabilitar uma aplicação específica para IPv6:
sudo ufw delete allow 'Nginx Full'

# 86. Permitir tráfego para um aplicativo personalizado em uma porta personalizada para IPv6:
sudo ufw allow 1234/tcp6

# 87. Desabilitar tráfego para um aplicativo personalizado em uma porta personalizada para IPv6:
sudo ufw delete allow 1234/tcp6

# 88. Habilitar tráfego para um aplicativo personalizado em uma porta personalizada e protocolo para IPv6:
sudo ufw allow proto tcp6 from any to any port 1234
