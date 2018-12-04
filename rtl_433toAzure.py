# https://azure.microsoft.com/en-us/documentation/articles/python-how-to-install/
# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html


from azure.servicebus import ServiceBusService, Message
import random, time, datetime, subprocess
from threading import Thread
from queue import Queue, Empty

#set up queueing to read and write lines as they come
io_q = Queue()

def stream_watcher(identifier, stream):
    
    for line in stream:
        io_q.put((identifier, line))

    if not stream.closed:
        stream.close()
        
def printer():
    while True:
        try:
            # Block for 1 second.
            item = io_q.get(True, 1)
        except Empty:
            # No output in either streams for a second. Are we done?
            if proc.poll() is not None:
                break
        else:
            identifier, line = item
            print(identifier + ':', line)

def pushToEventHub(sbs):
    while True:
        try:
            # Block for 1 second.
            item = io_q.get(True, 1)
        except Empty:
            # No output in either streams for a second. Are we done?
            if proc.poll() is not None:
                break
        else:
            identifier, line = item
            print(identifier + ':', line)
            if identifier == 'STDOUT':
                line = str(line)
                line = line[2:]
                line = line[:-3]
                try:
                    print(str(line))
                    sbs.send_event('kfcstoreeventhub', line)
                except:
                    pass
            elif str(line) == "Failed to open rtlsdr device #0.":
                break
            
# Azure Event Hub connection string
service_namespace = '<service namespace goes here>' 
key_name = '<key name goes here>' # SharedAccessKeyName from Azure portal
key_value = '<key value goes here>' # SharedAccessKey from Azure portal
sbs = ServiceBusService(service_namespace, shared_access_key_name=key_name,shared_access_key_value=key_value)

proc = subprocess.Popen(['rtl_433', '-R', '20', '-F', 'json','-d','0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

Thread(target=stream_watcher, name='stdout-watcher',
        args=('STDOUT', proc.stdout)).start()
Thread(target=stream_watcher, name='stderr-watcher',
        args=('STDERR', proc.stderr)).start()

Thread(target=pushToEventHub, name='pushToEventHub', args=([sbs])).start()
