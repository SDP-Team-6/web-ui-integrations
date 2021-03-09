import paramiko
import sys
from scp import SCPClient

IP = 'Pikachu' #IP Address of Raspberry Pi 
username = 'pi'
password = 'r00t'

def execute_command(cmd, client):
    print(f"Executing {cmd}")
    stdin_, stdout_, stderr_ = client.exec_command(cmd)
    status = stdout_.channel.recv_exit_status()
    print(f"STATUS {status}")
    for line in stdout_.readlines():
        print(line)
    if status != 0:
        errors = "\n".join(list(stderr_.readlines))
        raise Exception(f"{cmd} failed with {errors}")

def progress4(f, size, sent, p):
    prog = sent / size * 100.
    sys.stdout.write(f"({p[0]}:{p[1]}) {f}\'s progress: {prog}\r")

def ssh_connection():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(IP,username=username,password=password)
    
    execute_command('python /home/pi/paul/paul_controller.py', client)

if __name__ == '__main__':
    ssh_connection()



