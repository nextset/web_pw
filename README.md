## Web_pw
RUN!
```
source ./run.sh
```
## Docker for Debian 11 
```
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
```
```
apt-get update -y
apt-get install docker-ce docker-ce-cli -y
```
```
docker version
```
```
systemctl start docker
```
```
systemctl enable docker
```
```
systemctl status docker
```
## Docker Compose
```
sudo curl -L https://github.com/docker/compose/releases/download/1.25.3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
```
docker-compose --version
```