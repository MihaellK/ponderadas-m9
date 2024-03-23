# Conexão MQTT Hivemq - Ponderada 04 - M09

## Objetivo

Esse repositório tem como objetivo demonstrar a conexão de um publisher e subscriber em Go, junto a  um Cluster HiveMQ

## Setup

Antes de executar o código, é necessário instalar o [Go](https://rmnicola.github.io/m9-ec-encontros/go). Após isso siga as etapas abaixo:



## Executando

No terminal dentro do diretório, com o Cluster do HiveMQ configurado e um arquivo .env com o endereço do broker, seu usuario e senha cadastrado, execute o comando para instalar as dependencias:

```bash
go mod tidy
```
em seguida:
```bash
go run subscriber.go
```
em outro terminal:
```bash
go run publisher.go
```

## Resultados esperados

[Link do video](https://drive.google.com/file/d/1ab_8cbmfh1Uq9h_WXem1pr9onIvd-yJZ/view?usp=sharing)