# startup-local-comp

Automation script to startup and stop in windows (ollama in wsl):
- Open webui(docker)
- `ollama serve` in wsl
- Stable diffusion local webui using `--api` & `--listen`


In Open webui --> `http://host.docker.internal:7860/` is needed in the AUTOMATIC1111 Base URL in the Image Settings if it's being used this way...
Also if you're using Openedai-speech in docker, make sure you set the api address to `http://localhost:8000/v1` and the api key to `sk-111111111`
[text](https://github.com/matatonic/openedai-speech)

![image](https://github.com/wilarN/startup-local-companion/assets/68875195/c1bb34ed-7c48-4711-a399-e8283e1ac273)
![image](https://github.com/wilarN/startup-local-companion/assets/68875195/8f4b7af2-ddce-4bb9-8fd9-252ac9c88158)
![image](https://github.com/wilarN/startup-local-companion/assets/68875195/4651ca30-8466-4176-8b6d-1e4fea81df8e)
