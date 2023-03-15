# SocketServer
A simple Server framework in Python...

This server framework allows a client to run python programs (services) remotely on the server.

Place your python programs in the "Services" folder and adapt them to the structure shown in "service_base.py".

>__Note__
>If you need to use any external libraries, put them in the "lib" folder.

>__Warning__
>Service names cannot contain spaces or capital letters.

## Usage:

To Start the Server, run the following command in the console:

```
python Server.py
```

To Start the Client, run the following command in the console:

```
python Client.py
```

If you put '?' as a parameter, both will respond with a list of possible parameters.

>__Warning__
>Modifying the folder structure may cause errors!

>__Note__
>Only the "Client.py" file can be executed without being inside the project folder.
