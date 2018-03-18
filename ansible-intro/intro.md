# DevOps Workshops: Introduction to Ansible
{id: introduction-to-ansible}

## Slides
{id: slides}

https://code-maven.com/ws2

## About us
{id: about-us}

* Yonit Gruber-Hazani
* Gabor Szabo
* DevOps Workshops http://devops-workshops.code-maven.com/

## About you
{id: about-you}

* Name
* Company
* What do you do
* Something interesting about you
* Have you been to our first Linux meetup

## Prerequisites for the installations
{id: installation}

* Go to [https://code-maven.com/linux](https://code-maven.com/linux) to get the step by step instructions on how to install Linux on your laptop 

## my samples structure
{id: imagefortraining}

We are going to use one server and 2 hosts to train on, 
our network will look like: 

![ansible_structure](ansible_structure.jpg)


## Starting up - configuring the structure
{id: structure}

* [install the Ansible on the ansible server](http://docs.ansible.com/ansible/latest/intro_installation.html)

We will call this server the Ansible server
for ubuntu you can use these commands: 

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```

Than we want to configure the hosts file so it will know the other servers its working with:

```
sudo nano /etc/hosts
```

and add to its end:

```
192.168.56.10 ubuntu-1
192.168.56.20 ubuntu-2
```

save and exit
check by pinging the servers names:
ping ubuntu-1

also try to ssh both of them to verify connectivity.

## Configuring Ansible basic files
{id: conffiles}

* inventory file

This file describes the list of server and groups ansible is going to work on, 
our sample structure is going to be: 

```
[virtualhosts]
ubuntu-1
ubuntu-2

```

Ansible has some default location to add its config files, 
the install for ubuntu already creates the folder and basic files:

```
chown yonit ansible
chown yonit ansible/*
nano /etc/ansible/hosts
```

and add the lines above into it

## Running ansible
{id: runningansible}

there are 3 ways to run ansible: 

* running a command: ansible <group> -a <command>
* running a module: ansible <group> -m <module>
* running a playbook: ansible-playbook playbook.yml
  
[Ansible extensive list of builtin modules](http://docs.ansible.com/ansible/latest/modules_by_category.html)
trying our first command:

```
ansible virtualhosts -m ping
```

this will fail since we didnt setup the passwordless ssh.

```
ansible virtualhosts -m ping
SSH password:
ubuntu-1 | UNREACHABLE! => {
    "changed": false,
    "msg": "Authentication failure.",
    "unreachable": true
}
ubuntu-2 | UNREACHABLE! => {
    "changed": false,
    "msg": "Authentication failure.",
    "unreachable": true
}
```

## creating an ssh key file and passing it to the hosts
{id: sshkey}

[Mode details instructions](https://code-maven.com/generate-and-deploy-ssh-private-public-keypair)

```
ssh-keygen
ssh-copy-id ubuntu-1
ssh-copy-id ubuntu-2
```

from here ssh to the servers will be done without asking for password. 
make sure you have python installed on all the servers:

```
sudo apt-get update
sudo apt-get install --no-install-recommends --assume-yes python-apt
```

and lets try running the ansible command again:

```
yonit@ansible_server:/etc/ansible$ ansible virtualhosts -m ping
ubuntu-2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
ubuntu-1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## some more simple commands
{id: morecommands}

Go ahead and try some more: 

listing directories: 
ansible virtualhosts -a "ls -la /var"

install a package: 
ansible virtualhosts -m apt 

the apt command will fail - untill now we run everything with our user, 
to run commands as root we need to give passwordless sudo permission for the user we connect as: 

```
ssh ubuntu-1
sudo nano /etc/sudoers

and add this line:
yonit  ALL = (ALL) NOPASSWD: ALL
```

repeat for all the servers. 
lets try again: 

```
nsible virtualhosts -m apt -a "name=nginx state=present" -b
ubuntu-2 | SUCCESS => {
    "cache_update_time": 1521409853,
    "cache_updated": false,
    "changed": true,
    "stderr": "",
    "stderr_lines": [],
    "stdout": "Reading package lists...\nBuilding dependency tree...\nReading state information...\nThe following additional packages will be installed:\n  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0\n  libjpeg-turbo8 libjpeg8 libnginx-mod-http-geoip\n  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter\n  libnginx-mod-mail libnginx-mod-stream libtiff5 libwebp6 libxpm4 nginx-common\n  nginx-core\nSuggested packages:\n  libgd-tools fcgiwrap nginx-doc ssl-cert\nThe following NEW packages will be installed:\n  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0\n  libjpeg-turbo8 libjpeg8 libnginx-mod-http-geoip\n  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter\n  libnginx-mod-mail libnginx-mod-stream libtiff5 libwebp6 libxpm4 nginx\n  nginx-common nginx-core\n0 upgraded, 18 newly installed
```

lets check from one of the servers:

```
yonit@ubuntu-2:~$ service nginx status
   nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2018-03-19 00:15:24 IST; 1min 1s ago
     Docs: man:nginx(8)
```

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [introduction-to-ansible 80 minutes video](https://www.ansible.com/resources/webinars-training/introduction-to-ansible)