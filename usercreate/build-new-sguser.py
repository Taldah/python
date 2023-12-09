import tkinter as tk
import subprocess, time, sys
import signal, os, psutil, logging
import threading

def createAZADuser():
    #try:
     subprocess.Popen(['start', 'powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', "createAZUREADusers.ps1"], shell=True)
      # subprocess.run(['powershell.exe', "Import-Module AzureAD -UseWindowsPowerShell"], shell=False)
      # subprocess.run(['powershell.exe', "Import-Module -SkipEditionCheck -Name AzureAD"], shell=False)
      # subprocess.run(['powershell.exe', "connect-AzureAD"], shell=False)
      # subprocess.run(['powershell.exe', "Get-AzureADUser"], shell=False)
     #  subprocess.call(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', "C:\\Repos\\sg_tools\\usercreate\\createAZUREADusers.ps1"], stdout=sys.stdout, shell=True)
  #  except:
   #     print("File not Found")

def jirainvite():
    subprocess.call(['python.exe', './Apijira.py'], shell=True)


root = tk.Tk()

# --- Listbox ---

tk.Label(root, text='SG-UserCreate', bg='#aaa').pack(fill='x')
root.geometry('100x100')

#l = tk.Listbox(root)
#l.pack()
#l.insert('end')

# --- others ---
a = tk.Button(root, text='AzureAd-createuser', command=createAZADuser)
c = tk.Button(root, text='Quit', command=root.destroy)
b = tk.Button(root, text='invite-usertoJira', command=jirainvite)
a.pack(fill='x')
b.pack(fill='x')
c.pack(fill='x')




root.mainloop()