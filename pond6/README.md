# Integração entre o Kafka cloud e o HiveMQ

## Objetivo

Esse repositório demonstra a integração de um publisher mqtt no HiveMQ com o Kafka utilizando a integração propria do HiveMQ, permitindo que a integração ocorra no console Cloud da Plataforma

## Setup

Antes de executar o código, é necessário instalar o [Go](https://rmnicola.github.io/m9-ec-encontros/go). Após isso siga as etapas abaixo:

Também é necessario configurar um arquivo '.env' para acesso ao hivemq

```
BROKER_ADDR = <Seu HiveMQ Cluster URL>
HIVE_USER = <Usuario Credenciado>
HIVE_PSWD = <Senha do Usuario>

Bootstrap_server = <Endpoint do seu CLuster Confluent>
REST_endpoint = <REST Endpoint do Cluster Confluent>
```



## Executando

No terminal dentro do diretório, com seu .env configurado, seu usuario e senha cadastrado, execute o comando para instalar as dependencias:

```bash
go mod tidy
```
em seguida:
```bash
go run publisher
```

## Resultados

[Link do video](https://drive.google.com/file/d/1LhysMv_CQutt4047oJ8ieMN0RTPcw7S2/view?usp=sharing)