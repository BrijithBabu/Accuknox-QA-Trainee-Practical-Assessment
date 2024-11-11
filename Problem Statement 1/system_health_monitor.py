import psutil
import time
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low disk space detected: {disk_usage}% used")
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")
    return process_count

def monitor_system_health():
    while True:
        cpu = check_cpu_usage()
        memory = check_memory_usage()
        disk = check_disk_space()
        processes = check_running_processes()
        
        print(f"CPU Usage: {cpu}% | Memory Usage: {memory}% | Disk Usage: {disk}% | Running Processes: {processes}")
        
        time.sleep(5)  

if __name__ == "__main__":
    monitor_system_health()
