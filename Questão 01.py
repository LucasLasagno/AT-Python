import time
import psutil

processo = {}


def obter_info():
    for i in psutil.process_iter():
        if psutil.pid_exists(i.pid):
            processo[i.pid] = [
                i.name(),
                i.cpu_percent(),
                round(i.memory_percent(), 2)
            ]
        else:
            pass
    return processo

def resultado():
    print('{}{:<8}{:<12}{:<12}{:<12}'.format(' '*2, 'PID',
                                             'CPU %', 'MEM %', 'Nome'), sep='\n')

    # Aguardar 2 segundos para caso do arquivo não existir.
    time.sleep(1)
    for pid, info_pid in processo.items():
        print('{}{:<8}{:<12}{:<12}{:<12}'.format(
            ' '*2, pid, info_pid[1], info_pid[2], info_pid[0]))

        # Aguardar 2 segundos para caso do arquivo não existir.
        time.sleep(1)


obter_info()
resultado()