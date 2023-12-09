import tkinter as tk
import subprocess, time, sys
import signal, os, psutil, logging
import threading
from tkinter import *
# --- functions ---
def login():
    try:
        script = subprocess.call(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', "C:\\Repos\\support-projects\\check_folder.ps1"], stdout=sys.stdout)
        subprocess.call(['start', 'powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'C:\\Repos\\support-projects\\login_teleport.ps1'], shell=True)
    except OSError as Argument:
        # Creating/Opening a file:
        f = open("Logs.txt", "a")
        # writing in the file:
        f.write(str(Argument))
        # closing the file:
        f.close()
        raise

def on_button():
    #login = subprocess.call(['start', 'powershell.exe', 'C:\\Repos\\support-projects\\login_teleport.ps1'], shell=True)
    #vms == subprocess.Popen("C:\\Program Files (x86)\\VMS\\VMS.exe")
     #   subprocess.Popen("C:\\Program Files (x86)\\VMS\\VMS.exe")
    #time.sleep(10)

    shell = subprocess.Popen(['powershell.exe', '-command ', "write-host Open Teleport ssh"], shell=True)
# subprocess.run(['powershell.exe', '-command ', '$Env:PATH += ;C:\Program Files (x86)\Teleport'])
    #subprocess.run(['powershell.exe', '-command ', "tsh login --user tal@solargik.com --proxy=tele.solargik.com"])


    # different examples with `curselection()`

    for idx in l.curselection():
        if OPTIONS[idx] == 'camera-01-006-rfa':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[0]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[0]} --port 56000'], shell=False)
        elif OPTIONS[idx] == 'camera-01-015-akk-g24':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[1]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[1]} --port 46000'])
        elif OPTIONS[idx] == 'camera-02-015-akk-g25':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[2]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[2]} --port 39881'])
        elif OPTIONS[idx] == 'camera-01-001-mmc-r1':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[3]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[3]} --port 42484'])
        elif OPTIONS[idx] == 'camera-01-001-mmc-r2':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[4]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[4]} --port 46468'])
        elif OPTIONS[idx] == 'camera-018-afr-west':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[5]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[5]} --port 46446'])
        elif OPTIONS[idx] == 'camera-01-026-nbn':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[6]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[6]} --port 44800'])
        elif OPTIONS[idx] == 'cam-01-029-rap':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[7]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[7]} --port 42280'])
        elif OPTIONS[idx] == 'cam-01-022-ram-ea':
            subprocess.call(['powershell.exe', f'tsh apps login {OPTIONS[8]}'], shell=True) | subprocess.call(
                ['powershell.exe', f'tsh proxy app {OPTIONS[8]} --port 42525'])
        else:
            print('Timeout occurred')


def open_app():
    if "VMS.exe" in (i.name() for i in psutil.process_iter()):
        print("App allredy open")
    else:
      subprocess.call("C:\\Program Files (x86)\\VMS\\VMS.exe")

def close():
    subprocess.call(['powershell.exe', 'tsh apps logout'], shell=True)

def exit():
    try:
        root.destroy()
    except KeyboardInterrupt:
        # User interrupt the program with ctrl+c
        exit()


def multiprocess():
    threading.Thread(target=on_button).start()
def checktsh():
    threading.Thread(target=login).start()
def apps():
    threading.Thread(target=open_app).start()
def logout():
    threading.Thread(target=close).start()
def close_app():
    threading.Thread(target=exit).start()




#    subprocess.run(['powershell.exe', 'exit'])
 #   for idx in l.curselection():
 #       if idx == 0:
 #          print('Running first script')
 #       elif idx == 1:
 #          print('Running second script')
 #       elif idx == 2:
 #          print('Running third script')

 #   for idx in l.curselection():
 #          print('Running script:', OPTIONS[idx])

  #  for idx in l.curselection():
   #        print('Running script:', scripts[idx])

# --- main ---

#scripts = ["first.py", "second.py", "third.py"]

#OPTIONS = ["Script 1", "Script 2", "Script 3"]

OPTIONS = ["camera-01-006-rfa", "camera-01-015-akk-g24", "camera-02-015-akk-g25", "camera-01-001-mmc-r1", "camera-01-001-mmc-r2", "camera-018-afr-west", "camera-01-026-nbn", "cam-01-029-rap", "cam-01-022-ram-ea"]

root = tk.Tk()

# --- Listbox ---

tk.Label(root, text='Site-Names', bg='yellow', width=10).pack(fill='x')

l = tk.Listbox(root)
l.pack()
l.insert('end', *OPTIONS)


# --- others ---
a = tk.Button(root, text='Login-Teleport', command=checktsh)
b = tk.Button(root, text='Open-VMS', command=apps)
c = tk.Button(root, text='Login-PTZ', command=multiprocess)
d = tk.Button(root, text='Logout', command=close)
e = tk.Button(root, text='Quit', command=exit)
a.pack(fill='x')
b.pack(fill='x')
c.pack(fill='x')
d.pack(fill='x')
e.pack(fill='x')


root.mainloop()