###########################################################################
# Arquivo: gestao_containers_docker.txt                                    #
# Descrição: Exemplos soltos de comandos para gestão de containers Docker.#
# Criado por: Elias Andrade - Analista DevOps                             #
# LinkedIn: https://www.linkedin.com/in/elias-andrade-21574b2b4/          #
# Data: 15/02/2024                                                        #
###########################################################################

# Exemplos Solto de Gestão de Containers Docker:

# Criar e iniciar um novo container a partir da imagem nginx:
docker run -d --name meu_webserver -p 80:80 nginx

# Criar e iniciar um novo container a partir da imagem MySQL:
docker run -d --name meu_banco_dados -e MYSQL_ROOT_PASSWORD=minha_senha -p 3306:3306 mysql:latest

# Conectar-se a um container MySQL via cliente MySQL:
docker exec -it meu_banco_dados mysql -uroot -p

# Criar uma nova rede Docker:
docker network create minha_rede

# Conectar um container a uma rede específica:
docker network connect minha_rede meu_webserver

# Listar informações detalhadas sobre um container:
docker inspect meu_webserver

# Exibir os logs de um container em tempo real:
docker logs -f meu_webserver

# Parar todos os containers em execução:
docker stop $(docker ps -q)

# Remover todos os containers parados:
docker rm $(docker ps -aq)

# Exibir estatísticas de uso de recursos de um container:
docker stats meu_webserver

# Executar um comando dentro de um container em execução:
docker exec meu_webserver ls -l /var/www/html

# Criar uma imagem a partir de um container existente:
docker commit meu_webserver meu_imagem_customizada

# Exportar o sistema de arquivos de um container como um arquivo TAR:
docker export meu_webserver > meu_webserver.tar

# Importar um sistema de arquivos exportado como uma nova imagem:
cat meu_webserver.tar | docker import - minha_nova_imagem

# Executar um script dentro de um container:
docker exec -it meu_webserver sh /caminho/do/meu/script.sh

# Copiar arquivos do host para dentro de um container:
docker cp /caminho/do/meu/arquivo.txt meu_webserver:/caminho/no/container/

# Copiar arquivos de um container para o host:
docker cp meu_webserver:/caminho/no/container/arquivo.txt /caminho/do/meu/host/

# Iniciar um container pausado:
docker unpause meu_webserver

# Reiniciar um container em execução:
docker restart meu_webserver

# Executar um comando como usuário específico dentro de um container:
docker exec -u 1000 meu_webserver whoami

# Definir variáveis de ambiente ao executar um container:
docker run -e VARIAVEL=valor meu_imagem

# Exibir todos os containers, incluindo os parados:
docker ps -a

# Remover todos os containers, redes, imagens e volumes não utilizados:
docker system prune -a
