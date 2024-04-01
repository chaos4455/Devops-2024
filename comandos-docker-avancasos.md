###########################################################################
# Arquivo: comandos_docker_avancados.txt                                  #
# Descrição: Lista de comandos intermediários e completos do Docker.      #
# Criado por: Elias Andrade - Analista DevOps                             #
# LinkedIn: https://www.linkedin.com/in/elias-andrade-21574b2b4/          #
# Data: 15/02/2024                                                        #
###########################################################################

# Comandos Docker Intermediários e Completos:

51. docker pull nginx                                - Baixa a imagem do servidor web Nginx do Docker Hub.
52. docker pull ubuntu:20.04                         - Baixa a imagem do Ubuntu 20.04 do Docker Hub.
53. docker pull mysql:latest                         - Baixa a imagem mais recente do MySQL do Docker Hub.
54. docker pull node:14-alpine                      - Baixa a imagem do Node.js 14 na variante Alpine do Docker Hub.

55. docker build -t meu_app:1.0 .                    - Constrói uma imagem chamada "meu_app" a partir do Dockerfile no diretório atual.
56. docker build -f Dockerfile.dev -t meu_app:dev .  - Constrói uma imagem de desenvolvimento do aplicativo "meu_app" a partir de um Dockerfile específico.

57. docker create --name meu_container meu_imagem   - Cria um novo container chamado "meu_container" a partir da imagem "meu_imagem" sem iniciá-lo.
58. docker start -a meu_container                   - Inicia um container chamado "meu_container" e exibe os logs em tempo real.
59. docker stop meu_container                       - Para um container chamado "meu_container".
60. docker pause meu_container                      - Pausa a execução de um container chamado "meu_container".
61. docker unpause meu_container                    - Retoma a execução de um container chamado "meu_container".
62. docker restart meu_container                    - Reinicia um container chamado "meu_container".

63. docker rename meu_container novo_nome           - Renomeia um container de "meu_container" para "novo_nome".
64. docker update --cpu-shares 512 meu_container    - Define a quantidade de CPU compartilhada pelo container "meu_container".
65. docker update --memory 512m meu_container       - Define a quantidade de memória limite para o container "meu_container".

66. docker commit meu_container meu_imagem:1.0     - Cria uma nova imagem chamada "meu_imagem" a partir do estado atual do container "meu_container".

67. docker cp arquivo.txt meu_container:/diretorio  - Copia o arquivo "arquivo.txt" para o diretório dentro do container "meu_container".

68. docker exec -it meu_container bash             - Acessa o shell interativo dentro do container "meu_container".

69. docker top meu_container                        - Exibe os processos em execução dentro do container "meu_container".

70. docker stats                                    - Exibe estatísticas de uso de recursos de todos os containers em execução.

71. docker port meu_container                      - Exibe as portas mapeadas do container "meu_container".
72. docker port meu_container 80                   - Exibe a porta mapeada no host para a porta 80 do container "meu_container".

73. docker logs --tail 50 meu_container            - Exibe os últimos 50 registros de log do container "meu_container".

74. docker wait meu_container                      - Aguarda até que o container "meu_container" seja encerrado e retorna seu código de saída.

75. docker kill meu_container                      - Força a interrupção imediata do container "meu_container".

76. docker export meu_container > meu_container.tar - Exporta o sistema de arquivos do container "meu_container" como um arquivo TAR.

77. docker import meu_container.tar meu_imagem     - Cria uma nova imagem chamada "meu_imagem" a partir do arquivo TAR exportado.

78. docker save -o meu_imagem.tar meu_imagem      - Salva a imagem "meu_imagem" em um arquivo TAR.

79. docker load -i meu_imagem.tar                  - Carrega uma imagem previamente salva do arquivo TAR.

80. docker prune                                    - Remove todos os containers, redes, imagens e volumes não utilizados.

81. docker system prune                             - Remove todos os containers parados, redes não utilizadas, e imagens não referenciadas.

82. docker image prune                              - Remove imagens não utilizadas.

83. docker container prune                          - Remove containers parados.

84. docker volume prune                             - Remove volumes não utilizados.

85. docker network prune                            - Remove redes não utilizadas.

86. docker container pause meu_container           - Pausa a execução de um container chamado "meu_container".

87. docker container unpause meu_container        - Retoma a execução de um container chamado "meu_container".

88. docker container restart meu_container        - Reinicia um container chamado "meu_container".
