import options
import os
import psutil


def main():
    os.chdir(r'C:\VA_Test')
    os.system('start Vanessa_Start4_3.bat')
    for proc in psutil.process_iter():
        name = proc.name()
        print(name)
        if name == "1cv8c":
            print(name)
if __name__ == "__main__":
    main()