# Requisitos
-  [docker-ce](https://docs.docker.com/engine/install/ubuntu/)
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
# Como rodar
```sh
docker build -t quinto_andar .
docker run -v <path para pasta que vai salvar o modelo>:/tf/model --gpus all quinto_andar:latest
```
