sudo docker run -d --name local-vps-22 -p 22:22 -p 80:80  atlekbai/local-vps
ssh-copy-id -p 22 root@127.0.0.1