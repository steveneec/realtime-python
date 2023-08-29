# Realtime Chat Multiserver - Python

Este ejemplo implementa un chat en tiempo real usando sockets y python. Se hace uso de dos servidores simultanos conectados 
entre si que se comunican para poder enviar mensajes a clientes que estan conectados a el o a los del servidor secundario. 
Es decir se pueden comunicar todos los clientes, independientemente del servidor al que se hayan conectado

## Incializar el servidor
### Se deben iniciar dos instancias del servidor para funcionar

Iniciar el servidor con el comando

    python server.py <server_port> <secondary_server_port>

Los parametros que recibe el comando de inicializacion se describen a continuacion: <br>

    server_port -> el puerto que se quiere utilizar para el servidor principal
    secondary_server_port -> el puerto del servidor secundario

    #Ejemplo de inicializaciond de los servidores

    Servidor 1: python server.py 4001 4002
    Servidor 2: python server.py 4002 4001

El servidor se inicia usando la ip de loopback por lo que no es necesario configurarla a menos que se requiera usar desde dispositivos fisicos distintos

## Conectando clientes
### Los clientes deben especificar la ip del servidor y el puerto al que se quieren conectar, ademas de un nombre de usuario para identificarse

Se inicia el cliente con el comando

    python client.py <server_ip> <server_port> <user_name>

