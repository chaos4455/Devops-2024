###########################################################################
# Arquivo: comandos_docker.txt                                           #
# Descrição: Lista de comandos básicos do Docker.                         #
# Criado por: Elias Andrade - Analista DevOps                             #
# LinkedIn: https://www.linkedin.com/in/elias-andrade-21574b2b4/          #
# Data: 15/02/2024                                                        #
###########################################################################

# Comandos Docker Básicos:

1. docker version                 - Verifica a versão do Docker instalada.
2. docker info                    - Exibe informações do sistema Docker.
3. docker help                    - Mostra ajuda sobre comandos Docker.
4. docker search <nome_imagem>    - Pesquisa por imagens no Docker Hub.
5. docker pull <nome_imagem>      - Baixa uma imagem do Docker Hub.
6. docker images                  - Lista as imagens baixadas.
7. docker ps                      - Lista os containers em execução.
8. docker ps -a                   - Lista todos os containers.
9. docker run <nome_imagem>       - Executa um container a partir de uma imagem.
10. docker start <id_container>   - Inicia um container.
11. docker stop <id_container>    - Para um container em execução.
12. docker restart <id_container> - Reinicia um container.
13. docker rm <id_container>      - Remove um container.
14. docker rmi <nome_imagem>      - Remove uma imagem.
15. docker exec -it <id_container> <comando> - Executa um comando dentro do container.
16. docker logs <id_container>    - Exibe os logs de um container.
17. docker inspect <id_container> - Exibe detalhes de um container.
18. docker-compose --version      - Verifica a versão do Docker Compose.
19. docker-compose up             - Inicia os serviços definidos no arquivo docker-compose.yml.
20. docker-compose down           - Para e remove os serviços definidos no arquivo docker-compose.yml.
21. docker-compose ps             - Lista os serviços em execução.
22. docker-compose logs           - Exibe os logs dos serviços definidos no docker-compose.yml.
23. docker-compose exec <serviço> <comando> - Executa um comando dentro de um serviço.
24. docker network ls             - Lista as redes criadas no Docker.
25. docker network inspect <nome_rede> - Exibe detalhes de uma rede.
26. docker network create <nome_rede> - Cria uma nova rede.
27. docker network connect <nome_rede> <id_container> - Conecta um container a uma rede.
28. docker network disconnect <nome_rede> <id_container> - Desconecta um container de uma rede.
29. docker volume ls              - Lista os volumes criados no Docker.
30. docker volume inspect <nome_volume> - Exibe detalhes de um volume.
31. docker volume create <nome_volume> - Cria um novo volume.
32. docker volume rm <nome_volume> - Remove um volume.
33. docker build -t <nome_imagem> <caminho_dockerfile> - Constrói uma imagem a partir de um Dockerfile.
34. docker-compose build          - Constrói os serviços definidos no arquivo docker-compose.yml.
35. docker tag <nome_imagem> <nova_tag> - Adiciona uma nova tag a uma imagem.
36. docker push <nome_imagem>     - Faz o push de uma imagem para o Docker Hub.
37. docker pull <nome_imagem>:<tag> - Baixa uma imagem específica do Docker Hub.
38. docker run -d <nome_imagem>   - Executa um container em modo detached.
39. docker run -p <porta_host>:<porta_container> <nome_imagem> - Mapeia uma porta do host para o container.
40. docker run --name <nome_container> <nome_imagem> - Define um nome para o container ao executá-lo.
41. docker run -e <variável>=<valor> <nome_imagem> - Define variáveis de ambiente ao executar o container.
42. docker run -v <caminho_host>:<caminho_container> <nome_imagem> - Monta um volume ao executar o container.
43. docker run --rm <nome_imagem> - Remove o container automaticamente após sua execução.
44. docker exec -u <usuário> <id_container> <comando> - Executa um comando como um usuário específico dentro do container.
45. docker-compose up -d          - Inicia os serviços definidos no arquivo docker-compose.yml em modo detached.
46. docker-compose stop           - Para os serviços definidos no arquivo docker-compose.yml.
47. docker-compose restart        - Reinicia os serviços definidos no arquivo docker-compose.yml.
48. docker-compose logs -f        - Exibe os logs em tempo real dos serviços definidos no docker-compose.yml.
49. docker-compose exec <serviço> bash - Acessa o shell de um serviço no docker-compose.
50. docker-compose exec <serviço> <comando> - Executa um comando dentro de um serviço no docker-compose.
