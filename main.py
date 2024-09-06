import subprocess

import options
import os
import psutil
import time


def main():


    for proc in psutil.process_iter():
        PID = proc.pid
        name = proc.name()
        status = proc.status()

        print(f"PID [{PID}]\tNAME [{name}]\tSTATUS [{status}]")


if __name__ == "__main__":
    main()
