import os
import subprocess
import sys

# http://host.docker.internal:7860/

name_of_docker_container = "open-webui"

# Change this to your local path to the stable-diffusion-webui directory. This script uses the batch file to start the API. (webui.bat --api --listen)
directory_to_stable_diffusion_webui_absolute = "C://example//path//to//stable-diffusion-webui" # Change this to your path

starting = '''
                                                                                       
   _|_|_|    _|                            _|      _|                                  
 _|        _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|      _|_|_|      _|_|_|              
   _|_|      _|      _|    _|  _|_|        _|      _|  _|    _|  _|    _|              
       _|    _|      _|    _|  _|          _|      _|  _|    _|  _|    _|              
 _|_|_|        _|_|    _|_|_|  _|            _|_|  _|  _|    _|    _|_|_|  _|  _|  _|  
                                                                       _|              
                                                                   _|_|                
'''

stopping = '''
                                                                                       
   _|_|_|    _|                                    _|                                  
 _|        _|_|_|_|    _|_|    _|_|_|    _|_|_|        _|_|_|      _|_|_|              
   _|_|      _|      _|    _|  _|    _|  _|    _|  _|  _|    _|  _|    _|              
       _|    _|      _|    _|  _|    _|  _|    _|  _|  _|    _|  _|    _|              
 _|_|_|        _|_|    _|_|    _|_|_|    _|_|_|    _|  _|    _|    _|_|_|  _|  _|  _|  
                               _|        _|                            _|              
                               _|        _|                        _|_|                
'''

startup_script = """
                                                                                                                                 
   _|_|_|    _|                            _|                                _|_|_|                      _|              _|      
 _|        _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|  _|    _|  _|_|_|        _|          _|_|_|  _|  _|_|      _|_|_|    _|_|_|_|  
   _|_|      _|      _|    _|  _|_|        _|      _|    _|  _|    _|        _|_|    _|        _|_|      _|  _|    _|    _|      
       _|    _|      _|    _|  _|          _|      _|    _|  _|    _|            _|  _|        _|        _|  _|    _|    _|      
 _|_|_|        _|_|    _|_|_|  _|            _|_|    _|_|_|  _|_|_|        _|_|_|      _|_|_|  _|        _|  _|_|_|        _|_|  
                                                             _|                                              _|                  
                                                             _|                                              _|                 
"""

def start_all():
    print(starting)
    try:
        # ############### DOCKER OPEN WEBUI ###############
        print("Starting up Open WebUI docker container...")
        command = ["docker", "start", name_of_docker_container]
        subprocess.check_call(command, shell=False)

        # ########## STABLE DIFFUSION WEBUI API ###########
        print("Starting up Stable Diffusion WebUI API...")
        os.chdir(directory_to_stable_diffusion_webui_absolute)
        command = ["start", "cmd", "/c", "webui.bat --api --listen"]
        subprocess.Popen(command, shell=True)

        # ############### OLLAMA SERVE ####################
        print("Starting up Ollama Serve...")
        command = ["start", "wsl", "ollama", "serve"]
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print("Error starting up: ", e)

    print("[ All services started successfully. ]")
    print("Dont forget to add http://host.docker.internal:7860/ to the Open WebUI's image gen API.")
    print("Open the webgui: http://localhost:3000/")

def stop_all():
    print(stopping)
        # ############### DOCKER OPEN WEBUI ###############
    try:
        print("Stopping Open WebUI docker container...")
        command = ["docker", "stop", name_of_docker_container]
        subprocess.check_call(command, shell=False)
    except Exception as e:
        print("Error stopping Open WebUI docker container: ", e)

        # ########## STABLE DIFFUSION WEBUI API ###########
    try:
        print("Stopping Stable Diffusion WebUI API...")
        os.chdir(directory_to_stable_diffusion_webui_absolute)
        command = ["taskkill", "/IM", "python.exe", "/F"]
        subprocess.check_call(command, shell=False)
    except Exception as e:
        print("Error stopping Stable Diffusion WebUI API: ", e)

        # ############### OLLAMA SERVE ####################
    try:
        print("Stopping Ollama Serve...")
        command = ["wsl", "killall", "ollama"]
        subprocess.run(command, check=True)
        print("Ollama Serve stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping Ollama Serve: {e}")

    print("[ All services stopped successfully. ]")

def main():
    if start:
        start_all()
    else:
        stop_all()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(startup_script)
        print("Invalid argument\nUsage: python3 startup.py --start/--stop")
        exit(1)
    if sys.argv[1] == "--start":
        start = True
    elif sys.argv[1] == "--stop":
        start = False
    else:
        print(startup_script)
        print("Invalid argument\nUsage: python3 startup.py --start/--stop")
        exit(1)

    main()
