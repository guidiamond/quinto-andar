# Requisitos
-  [docker-ce](https://docs.docker.com/engine/install/ubuntu/)
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
# Como rodar
```sh
docker build -t quinto_andar .
docker run -v <path para pasta que vai salvar o modelo>:/app --gpus all quinto_andar:latest
```

# Como configurar o s3fs
Para usar o s3 como uma pasta desse computador, é necessário instalar o pacote [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse):
Para configurá-lo basta rodar os seguintes comandos:
```sh
# Colocar credenciais para acessar a aws
echo ACCESS_KEY_ID:SECRET_ACCESS_KEY > ${HOME}/.passwd-s3fs
chmod 600 ${HOME}/.passwd-s3fs

# Colocar o path (absoluto) da pasta que vc quer que tenha os arquivos do s3 (parecido com o dropbox/onedrive)
s3fs mybucket <path to mountpoint> -o passwd_file=${HOME}/.passwd-s3fs
```

Rodando os comando acima, qualquer alteração (leitura/escrita/apagar) feita nessa pasta reflete diretamente no bucket.
