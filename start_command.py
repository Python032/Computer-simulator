from tkinter import *
import turtle as t
import random
import time
import datetime
import requests
import help
import paint

# system regdit "regdit.exe"
regdit_apps_note_stop_math = 30
regdit_start_run_new_password = False
regdit_runsystem_command = True
regdit_start_text = "Welcome!"
regdit_stop_sleep_time = 2
regdit_stop_text = "Goodbye!"
regdit_user_name = "huyaoyu"
regdit_user_password = "123456"
regdit_note_file = "new.disk"
regdit_log_file = "py_log.log_py"
regdit_log_mode = "a"
regdit_logs = open(regdit_log_file,regdit_log_mode)
regdit_system_v = "1.4"
regdit_error_list = [
    "Error 001: PASSWORD OR NAME ERROR"
]
regdit_code_list = [
    "forcibly_stop","exit","cls","note","suspend","net_text","read_disk","th","disk_config",
    "this_command","del_disk","for_system","paint","default_message"
]
regdit_value = [regdit_apps_note_stop_math,regdit_start_run_new_password,regdit_runsystem_command,
regdit_start_text,regdit_stop_sleep_time,regdit_stop_text,regdit_user_name,regdit_user_password,
regdit_note_file,regdit_log_file,regdit_log_mode,regdit_logs,regdit_system_v,regdit_error_list
]

# system update class "runsystem.exe"
class system_update:
    def run():
        run_condition = regdit_runsystem_command
        print("The system is checking for important tools...")
        firewall.run_tools("inspect")
        print("\nDone.")
        print('You can use the "help" command to get all the commands')
        regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ User login] [info]")
        while run_condition == True:
            inputs_text_for_command = input(">>>>>>")
            if inputs_text_for_command == "forcibly_stop":
                system_stop.force_stop()
            if inputs_text_for_command == "exit":
                system_stop.stop()
            if inputs_text_for_command == "cls":
                apps.cls()
            if inputs_text_for_command == "note":
                apps.note()
            if inputs_text_for_command == "suspend":
                system_stop.screen_saver()
            if inputs_text_for_command == "net_text":
                system_net.net_text()
            if inputs_text_for_command == "read_disk":
                apps.read_disk()
            if inputs_text_for_command == "th":
                apps.text()
            if inputs_text_for_command == "disk_config":
                apps.file_config()
            if inputs_text_for_command == "this_command":
                apps.this_command()
            if inputs_text_for_command == "del_disk":
                apps.del_disk()
            if inputs_text_for_command == "for_system":
                help.start()
            if inputs_text_for_command == "paint":
                paint.window.paint()
            if inputs_text_for_command == "default_message":
                message.default(input("Print text:"))
            if inputs_text_for_command == "help":
                print(regdit_code_list)
            regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ User input:"+inputs_text_for_command+"] [info]")

    def welcome():
        if regdit_start_run_new_password == True:
            print("-------------|x|")
            print("|New password? |")
            print("--YES------NO---")
            password_factor = input("Factor:")
            if password_factor == "No":
                system_update.run()
            elif password_factor == "Yes":
                new_password_text = input("New password:")
                print("--An unknown error has occurred--")
                system_update.run()
        else:
            system_update.run()

# system stop classmethod "shutdown.exe"
class system_stop:
    def force_stop():
        print("--------------------------------------------")
        print("|Do you want to forcibly stop the console? |")
        print("------------------------------YES------NO---")
        forcibly_stop_text = input("Yes or No:")
        if forcibly_stop_text == "Yes":
            quit()
        elif forcibly_stop_text == "No":
            system_update.run()
    def stop():
        print(regdit_stop_text)
        time.sleep(regdit_stop_sleep_time)
        regdit_logs.close()
        exit()
    def screen_saver():
        t.speed(0)
        t.penup()
        for i in range(100):
            t.title("suspend")
            t.goto(random.randint(-300,300),random.randint(-300,300))
            t.pendown()
            regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ Suspend start] [info]")
            for s in range(4):
                t.forward(50)
                t.left(90)
            t.write(i)
            t.penup()
            regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ Suspend end] [info]")

# system all apps
class apps:
    def cls():
        input_cls_help = int(input("option(1=* 2=/ 3=+ 4=-):"))
        if input_cls_help == 1:
            cls_ce_one = int(input("one math:"))
            cls_ce_tow = int(input("tow math:"))
            print(cls_ce_one * cls_ce_tow)
        if input_cls_help == 2:
            cls_cu_one = int(input("one math:"))
            cls_cu_tow = int(input("tow math:"))
            print(cls_cu_one / cls_cu_tow)
        if input_cls_help == 3:
            cls_ja_one = int(input("one math:"))
            cls_ja_tow = int(input("tow math:"))
            print(cls_ja_one + cls_ja_tow)
        if input_cls_help == 4:
            cls_jn_one = int(input("one math:"))
            cls_jn_tow = int(input("tow math:"))
            print(cls_jn_one - cls_jn_tow)
    def note():
        files = open(input("File or Disk name:"),"a")
        files.write("\n")
        files.write(str(datetime.datetime.now()))
        files.write("\n")
        print("note book__________________________")
        i = 0
        while True:
            texts = input("|"+str(i+1)+"  ")
            if texts == "end":
                break
            files.write(texts)

            files.write("\n")
            regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ User note text:"+texts+"] [info]")
        files.close()
        print("____________________________________")
    def read_disk():
        data = input("Disk name:")
        print(open(data,"r").read())
    def text():
        print("|-Text thml v1.0----------Colse'c'-|")
        data = input("| File name(*.th):")
        print("| "+str(datetime.datetime.now()))
        print("| "+open(data,'r').read())
        print("|----------------------------------|")
    def file_config():
        print("|-Files config------------------------|")
        print("| nd=New disk nth=New th    e=Exit    |")
        print("|-------------------------------------|")
        command = input("Command:")
        if command == "nd":
            disk_name = input("Disk name:")
            open(disk_name+".disk","w")
        if command == "nth":
            disk_name = input("*.th file name:")
            open(disk_name+".th","w")
        if command == "e":
            pass
    def this_command():
        root = Tk()
        root.title("THIS COMMAND V1.0")
        root.geometry("200x50")
        l1 = Label(root,text="The computer from HUYAOYU.")
        l2 = Label(root,text="(V1.0)")
        l1.pack()
        l2.pack()
    def del_disk():
        data = input("Disk name:")
        sensitive_words = ["help.py","run.py","paint.py",
        "read_text.py","py_log.log_py","start_command.py"]
        if data in sensitive_words:
            print("Sorry, the file name you entered contains sensitive words because it is an important file in this system.")
            return
        else:
            open(data,"w")
            message.app_message_stort("Done")

# system net "net.exe"
class system_net:
    def net_text():
        net_url = input("URL:")
        strhtml = requests.get(net_url)
        print("net text_____________________________________________________________")
        print(strhtml.text)
        print("_____________________________________________________________________")
        regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ User URL:"+net_url+"] [info]")

# system start class "open_system.exe"
class system_start:
    def logon_true():
        print(regdit_start_text)
        system_update.welcome()
    def logon_false():
        print("Your name or password is wrong.")
        message.error(0)
        time.sleep(regdit_stop_sleep_time)
    def logon(username="",password=""):
        message.app_message_stort("login")
        input_username = input("your name:")
        input_password = input("your password:")
        username = input_username
        password = input_password
        if input_username == regdit_user_name and input_password == regdit_user_password:
            regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ User name and password is right."+" name:"+username+" password:"+input_password+"]"+" [info]")
            system_start.logon_true()
        else:
            regdit_logs.write("\n["+str(datetime.datetime.now())+"] [ User name or password is wrong."+" name:"+username+" password:"+input_password+"]"+" [error]")
            system_start.logon_false()

# message window "message.exe"
class message:
    def default(text=None):
        print("#"*(len(str(text))+4))
        print("# "+str(text)+" #")
        print("#"*(len(str(text))+4))
    def error(list_number=int):
        print("#"*(len(regdit_error_list[list_number])+4))
        print("# "+regdit_error_list[list_number]+" #")
        print("#"*(len(regdit_error_list[list_number])+4))
    def app_message_stort(stort_text=None):
        print("#"*10+"  "+str(stort_text)+"  "+"#"*10)
    def app_message_long(long_text=None):
        print("#"*(len(str(long_text))+4))
        print("# "+str(long_text)+" #")
        print("#"*(len(str(long_text))+4))

class firewall:
    def run_tools(mode=str):
        if mode == "inspect":
            def easy():
                print("NO.1 class:message")
                message.default("    ")
                message.error(0)
                message.app_message_long("    ")
                message.app_message_stort("     ")
                print("done.")
                print("NO.2 class:system_start")
                system_start.logon_false()
                print("done.")
                print("NO.3 all regdit")
                print(regdit_value)
            easy()

system_start.logon()