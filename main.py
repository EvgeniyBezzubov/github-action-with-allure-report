import options
import os
import psutil
import time


def main():
 ##   os.chdir(r'C:\VA_Test')
   ## os.system('start Vanessa_Start4_3.bat')
    print(psutil.cpu_stats())
    print(1234)
    ##time.sleep(15)


    os.chdir(r'C:\VA_Test')


    asas = os.system(r'runas / user: TestUser Vanessa_Start4_3.bat')



   # status = ""


   # for proc in psutil.process_iter(['pid', 'name', 'username']):
   #     proc.username()
    #    print(proc.info)


if __name__ == "__main__":
    main()
