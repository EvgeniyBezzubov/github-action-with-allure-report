import subprocess
import os
import psutil
import time


def main():
    massive_opt = load_params()
    PathTo1c = massive_opt["PathTo1c"]
    PathToBaseManager = massive_opt["PathToBaseManager"]
    PathParams = massive_opt["PathParams"]
    PathToBaseClient = massive_opt["PathToBaseClient"]
    PathToVanessa = massive_opt["PathToVanessa"]
    timeOnRun = massive_opt["timeOnRun"]
    PathToProject = massive_opt["PathToProject"]

    end_1c_process = True
    retreat_num = 0

    while end_1c_process:

        if retreat_num == 0:
            Manager = subprocess.Popen([PathTo1c,
                                        " /N Администратор /TestManager  /Execute " + PathToVanessa + " /IBConnectionString" + f"File={PathToBaseManager}" ]) ##+ f"; /C StartFeaturePlayer;VAParams=C:/Users/User/PycharmProjects/pythonProject1/VAParams5.json"
            Client = subprocess.Popen([PathTo1c,
                                       " /N Администратор /TESTCLIENT -TPort 48132 " + " /IBConnectionString" + f"File={PathToBaseClient}"])
            ProcManagerIsRun = True
            ProcClientIsRun = True

        retreat_num +=1

        print(Manager.pid)
        print(Client.pid)
        try:
            ManagerProc = psutil.Process(Manager.pid)
        except:
            ProcManagerIsRun = False
            print("Процесс менеджер не найден")

        try:
            ClientProc  = psutil.Process(Client.pid)
        except:
            print("Процесс клиент не найден")
            ProcClientIsRun = False
        if retreat_num > int(timeOnRun):
            if ProcManagerIsRun:
                ManagerProc.kill()
                ProcManagerIsRun = False
            if ProcClientIsRun:
                ClientProc.kill()
                ProcClientIsRun = False
          ##  os.system("call allure generate --clean " + PathToProject + "\some")

            os.system("cd " + PathToProject)
            os.system("git add .")
            os.system(f'git commit -m "Автозапуск"')
            os.system("git push")

        if not ProcClientIsRun and not ProcManagerIsRun:
            os.system("git add .")
            os.system(f'git commit -m "Автозапуск"')
            os.system("git push")
            break
        time.sleep(1)
def load_params():
    f = open("options.txt")
    opions_word = {}
    for opt in f:
        list_options = opt.split(" = ")
        list_stab_options = []
        for i in list_options:
            list_stab_options.append(i.rstrip('\n'))
        list_options = list_stab_options
        opions_word[list_options[0]] = list_options[1]
    f.close()
    return opions_word


if __name__ == "__main__":
    main()