import os
import subprocess
import sys
# http://host.docker.internal:7860/

name_of_docker_container = "open-webui"
directory_to_stable_diffusion_webui_absolute = "C://DEV//AI_GEN_THING//stable-diffusion-webui//"


def start_all():
    print("Starting up...")
    # ############### DOCKER OPEN WEBUI ###############
    print("Starting up Open WebUI docker container...")
    command = ["docker", "start", name_of_docker_container]
    subprocess.check_call(command, shell=False)

    # #################################################

    # ########## STABLE DIFFUSION WEBUI API ###########
    print("Starting up Stable Diffusion WebUI API...")
    os.chdir(directory_to_stable_diffusion_webui_absolute)
    command = ["start", "cmd", "/c", "webui.bat --api --listen"]
    subprocess.Popen(command, shell=True)

    # #################################################

    # ############### OLLAMA SERVE ####################
    print("Starting up Ollama Serve...")
    command = ["wsl", "ollama", "serve"]
    subprocess.Popen(command, shell=True)


def stop_all():
    try:
        print("Shutting down...")

        # List all container
        os.system("docker ps -a")

        # ############### DOCKER OPEN WEBUI ###############
        print("Stopping Open WebUI docker container...")
        command = ["docker", "stop", name_of_docker_container]
        subprocess.check_call(command, shell=False)

        # #################################################

        # ########## STABLE DIFFUSION WEBUI API ###########
        print("Stopping Stable Diffusion WebUI API...")
        os.chdir(directory_to_stable_diffusion_webui_absolute)
        command = ["taskkill", "/IM", "python.exe", "/F"]
        subprocess.check_call(command, shell=False)

        # #################################################

        # ############### OLLAMA SERVE ####################
        print("Stopping Ollama Serve...")
        command = ["taskkill", "/IM", "/F"]
        subprocess.check_call(command, shell=False)

        # #################################################
    except Exception as e:
        print("Error: ", e)


def main():
    if start:
        start_all()
    else:
        stop_all()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid argument\nUsage: python startup.py --start/--stop")
        exit(1)
    if sys.argv[1] == "--start":
        start = True
    elif sys.argv[1] == "--stop":
        start = False
    else:
        print("Invalid argument\nUsage: python startup.py --start/--stop")
        exit(1)

    main()
