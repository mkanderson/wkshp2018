### Lab 1 > SSH Client Einrichten, Login, erste Schritte auf der Kommandozeile

**Voraussetzungen**: installierter SSH Terminal Client, Zugangsdaten

`ssh` `hostname` `pwd` `whoami`

---
##### `Aufgabe` SSH-Client Installieren

Installieren Sie der passende SSH-Client für Ihre Betriebsystem.

* **Linux und MacOS**

 Praktisch alle aktuelle Linux-Distributionen werden mit einem SSH client mitgeliefert. Falls ein SSH-Client nicht installiert ist, kann es mit dem Paketmanager nachinstalliert werden, beispielsweise hier auf Debian Linux:
```
sudo apt-get install openssh-client
```

* **MS-Windows**

 PuTTY ist ein Terminal und SSH Client für Microsoft Windows. Das Installationspaket kann hier heruntergeladen werden:

 https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html


---
##### `Aufgabe` Verbinden mit einem Remote Host 

* **Linux/MacOS**

 `ssh <user>@<host.domain>`

 _Beispiel:_

 ```
[admin@localhost: ~]$ ssh user1@srv01.elegobox.com 
Linux stan 4.9.0-7-amd64 #1 SMP Debian 4.9.110-1 (2018-07-05) x86_64
Last login: Wed Sep 26 21:31:17 2018 from 87.122.81.53
user1@srv01:~# 
```


* **Windows/PuTTY**




