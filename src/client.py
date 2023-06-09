from logInPage_GUI import LogIn_Page_UI
from homePage_GUI import HomePage_UI
import shutdown_logout_client as sl
import mac_address_client as mac
import keylogger_client as kl
import app_process_client as ap
import directory_tree_client as dt
import live_screen_client as lsc
import registry_client as rc

import socket
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import*

#global variables
BUFSIZ = 1024 * 4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

app = Tk()
app.geometry("1000x600")
app.configure(bg = "#FFFFFF")
app.title('Client')
app.resizable(False, False)
frame_lg = LogIn_Page_UI(app)



def back(temp):
    temp.destroy()
    frame_hp.tkraise()
    client.sendall(bytes("QUIT", "utf8"))

def liveCreen():
    client.sendall(bytes("LIVESCREEN", "utf8"))
    temp = lsc.Desktop_UI(app, client)
    if temp.status == False:
        back(temp)
    return

def mac_address():
    client.sendall(bytes("MAC", "utf8"))
    mac.mac_address(client)
    return

def disconnect():
    client.sendall(bytes("QUIT", "utf8"))
    frame_hp.destroy()
    app.destroy()
    return
 

def keylogger():
    client.sendall(bytes("KEYLOG", "utf8"))
    temp = kl.Keylogger_UI(app, client)
    temp.button_back.configure(command = lambda: back(temp))
    return

def app_process():
    client.sendall(bytes("APP_PRO", "utf8"))
    temp = ap.App_Process_UI(app, client)
    temp.button_back.configure(command = lambda: back(temp))
    return

def back_reg(temp):
    temp.client.sendall(bytes("STOP_EDIT_REGISTRY", "utf8"))
    temp.destroy()
    frame_hp.tkraise()

def directory_tree():
    client.sendall(bytes("DIRECTORY", "utf8"))
    temp = dt.DirectoryTree_UI(app, client)
    temp.button_6.configure(command = lambda: back(temp))
    return

def registry():
    client.sendall(bytes("REGISTRY", "utf8"))
    temp = rc.Registry_UI(app, client)
    temp.btn_back.configure(command=lambda: back_reg(temp))
    return

def shutdown_logout():
    client.sendall(bytes("SD_LO", "utf8"))
    temp = sl.shutdown_logout(client, app)
    return

def show_main_ui():
    frame_lg.destroy()
    global frame_hp
    frame_hp = HomePage_UI(app)
    frame_hp.button_live_creen.configure(command = liveCreen)
    frame_hp.button_mac_address.configure(command = mac_address)
    frame_hp.button_disconnect.configure(command = disconnect)
    frame_hp.button_keylogger.configure(command = keylogger)
    frame_hp.button_AppProcess.configure(command = app_process)
    frame_hp.button_directoryTree.configure(command = directory_tree)
    frame_hp.button_registry.configure(command = registry)
    frame_hp.button_shut_down.configure(command = shutdown_logout)
    return

def connect(frame):
    global client
    ip = frame.entry_1.get()
    try:
        client.connect((ip, 5656))
        messagebox.showinfo(message = "Connect successfully!")
        show_main_ui()
    except:
        messagebox.showerror(message = "Cannot connect!")       
    return 

def main():
    frame_lg.button_1.configure(command= lambda:connect(frame_lg))
    app.mainloop()

if __name__ == '__main__':
    main()