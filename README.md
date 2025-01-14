# IP-retriever
This application uses python to retireve the IP address of the device it is running on then shares it to an mqtt broker under the topic WIFI, it also listens for a message on the same mqtt brocker under the topic getIP this trggers the action to get the IP address. The code for all this is in the RasberyClient.py

## Remote client
The DemoRemoteClient.py show how a remote client would use mqtt to request for the ip

## Front-end
There is a front-end written in vue that will connect to the mqtt brocker to retrive and display the ip this can be found in ip app