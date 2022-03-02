#Crear un Pool de Hilos para fuerza bruta grandes.

import requests
import base64
import logging
import queue, threading
import time

start = time.process_time()
#En requests no hace falta encodear los parámetros. Requests lo hace por si solo. En el ejemplo del data.
'''
Metodo para ver los logs. MUY UTIL.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
'''

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

tarjetas_List = open('tarjetas.txt','r').read().splitlines() # El valor que necesitas iterar.
#print (tarjetas_List)

class WorkerThread(threading.Thread):

    def __init__(self, queue, tid):
        threading.Thread.__init__(self)
        self.queue = queue
        self.tid = tid

    def run(self):
        while True:
            phone = None

            try:
                tarjeta = self.queue.get(timeout=1)

            except    queue.Empty:
                return

            try:
                #Aqui se pone las peticiones de la fuerza bruta
                burp0_url = "XXXXXXX"
                burp0_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                

            except:
                raise

            self.queue.task_done()


queue = queue.Queue()

threads = []
for i in range(1, 100):  # Number of threads
    worker = WorkerThread(queue, i)
    worker.setDaemon(True)
    worker.start()
    threads.append(worker)
    # threads.join()

for tarjeta in tarjetas_List:  # Rellename ceros
    queue.put(tarjeta)

queue.join()

# wait for all threads to exit

for item in threads:
    item.join()

print("Bruteforce Complete!")

