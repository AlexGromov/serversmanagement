from Queue import Queue, Empty
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep
from app import models
import random
import config

#TODO: fix it!
class NonBlockingStreamReader:

    def __init__(self, stream):
        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            while True:
                line = stream.readline()
                if line:
                    queue.put(line)

        self._t = Thread(target = _populateQueue, args = (self._s, self._q))
        self._t.daemon = True
        self._t.start()

    def readline(self, timeout = None):
        try:
            return self._q.get(block = timeout is not None, timeout = timeout)
        except Empty:
            return None

def get_server():
    #TODO: get env_per_server variable
    """
    get random not loaded server
    """
    
    #TODO: model's class method???
    server_list = models.Server.query.filter_by(state=config.server_state['on']).all()
    if server_list:
        return random.choice(server_list).id  
    return None

def run_task(task_name, task_file, task_auth):
    
    #TODO: --abort-on-prompts=True
    
    #TODO: use fabric API
    cmd = 'fab -R %s %s --fabfile=%s'  % (task_auth, task_name, task_file)
    p = Popen(cmd, stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = True)
    #TODO: save pid
    #+ output http://docs.fabfile.org/en/latest/usage/output_controls.html
    
    #TODO: update task state
    nbsr = NonBlockingStreamReader(p.stdout)
    cmd_out = nbsr.readline(1)
    return cmd_out

def scheduler():
    """
    get run_id fitered by lower id
    """ 
    pass
     