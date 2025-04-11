import os, sys
import platform as p
import subprocess
import getpass

if p.system() == 'Linux':
    print("Running in Linux")

    create_user = f"CREATE USER {getpass.getuser()} WITH PASSWORD '123';"
    #sql = 'SELECT version();'
    alter_role = f"ALTER ROLE {getpass.getuser()} WITH SUPERUSER;"
    create_db = f"CREATE DATABASE llm_db;"
    grant_priv = f"GRANT ALL PRIVILEGES ON DATABASE llm_db TO {getpass.getuser()};"
    exit = 'exit'

    command = ['sudo', '-i', '-u', 'postgres', 'psql', '-c', 
               create_user, alter_role, create_db]

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()

    if (error.decode('utf-8')):
        print('Error:\n' + error.decode('utf-8'))
    else:
        if (proc.returncode == 0):
            print('Output:\n>' + output.decode('utf-8'))
    print('Exit code:', proc.returncode)

    proc.kill()

    command2 = ['psql', '-U', getpass.getuser(), '-d', 'llm_db']
    proc = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()
    if (error.decode('utf-8')):
        print('Error:\n' + error.decode('utf-8'))
    else:
        if (proc.returncode == 0):
            print('Output:\n>' + output.decode('utf-8'))
    print('Exit code:', proc.returncode)