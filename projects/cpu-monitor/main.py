import os
os.system("pip install psutil")
os.system("zenity --version")

import psutil

def Reload():
    dictionaryBase = {
        "cpu_percent": (psutil.cpu_percent(interval = 1)),
        "memory_percent": psutil.virtual_memory().percent,
        "memory_total": int(psutil.virtual_memory().total / 1048576),
        "memory_available": int(psutil.virtual_memory().available / 1048576),
        "memory_used": int(psutil.virtual_memory().total / 1048576 - psutil.virtual_memory().available / 1048576)
    }
    # return json.dumps(dictionaryBase)
    return dictionaryBase


main = Reload()
zenity = f'zenity --list --title "CPU Monitor" --text "" --width 700 --column "CPU" --column "Memory Percent" --column "Memory Available" --column "Memory Used" --column "Memory Total" {main["cpu_percent"]}% {main["memory_percent"]}% {main["memory_available"]}MB {main["memory_used"]}MB {main["memory_total"]}MB'
os.system(zenity)
