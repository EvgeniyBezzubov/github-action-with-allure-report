import options
import os
import psutil
import time

def main():
    os.chdir(r'C:\VA_Test')
    os.system('start Vanessa_Start4_3.bat')
    time.sleep(15)
    status = ""
    for proc in psutil.process_iter():
        name = proc.name()
        print(proc)
        if name == "1cv8c":
            print(proc.create_time())
            status = "Run"
        else:
            status = "not Run"
            return 0

    time.sleep(200)

    for proc in psutil.process_iter():
        name = proc.name()
        if name == "1cv8c":
            status = "Error "
        else:
            status = "not Run"
            return 0

if __name__ == "__main__":
    main()