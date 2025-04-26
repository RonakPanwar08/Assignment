import psutil
import socket
import requests
import json


BACKEND_URL = "http://127.0.0.1:8000/api/process-data/"
API_KEY = "your-api-key"  

def get_process_data():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'ppid']):
        try:
            parent_name = psutil.Process(proc.info['ppid']).name() if proc.info['ppid'] else None
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu": proc.info['cpu_percent'],
                "memory": round(proc.info['memory_percent'], 2),
                "parent_pid": proc.info['ppid'],
                "parent_name": parent_name
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def send_data():
    hostname = socket.gethostname()
    data = {
        "hostname": hostname,
        "processes": get_process_data()
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_KEY}"
    }
    try:
        response = requests.post(BACKEND_URL, headers=headers, json=data)
        print("Data sent:", response.status_code)
    except Exception as e:
        print("Failed to send data:", e)

if __name__ == '__main__':
    send_data()
