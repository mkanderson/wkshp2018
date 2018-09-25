# Befehlsübersicht

### Grundkommandos

`cat`           Verknüpfung von Dateien ("concatenate")

`cd`            Wechsel des Arbeitsverzeichnisses ("change directory")

`cp`            Kopie von Dateien oder Verzeichnissen ("copy")

`date`          Anzeige von Datum und Zeit

`echo`          Anzeige eines Textes

`exit`          Ende der Sitzung

`ln`            Link zu einer Datei oder einem Verzeichnis ("link")

`ls`            Auflistung von Dateien ("list")

`man`           Ausgabe der Handbuchseite zu einem Befehl oder einer Anwendung ("manual")

`mkdir`         Erzeugung von Verzeichnissen ("make directory")

`mv`            Kopieren einer Datei und Löschen der Ursprungsdatei ("move"); mv im aktuellen Verzeichnis ausgeführt: Umbenennung einer Datei

`pwd`           Anzeige des aktuellen Verzeichnisses ("print working directory")

`rm`            Löschen von Dateien und Verzeichnisse ("remove")

`rmdir`         Löschen eines leeren Verzeichnisses ("remove directory")

`sudo`          Root-Rechte für den Benutzer ("substitute user do")

`touch`         Änderung der Zugriffs- und Änderungszeitstempel einer Datei oder eines Verzeichnisses (auch: Erstellen von Dateien)

`clear`         Dieser Befehl löscht den Inhalt des sichtbaren Konsolenausschnitts. Er verfügt über keine Optionen.

`halt`          Um keinen Datenverlust zu riskieren, sollten Sie Ihr System immer mit diesem Programm herunterfahren. 

`reboot`        Fährt das System wie mit dem Befehl halt herunter, startet es aber unmittelbar danach wieder.

---

### Befehl Syntax und Häufig verwendete Optionen von Grundkommandos

ls [Optionen] [Dateien] 

    -l          Zeigt eine detaillierte Liste an.
    -a          Zeigt versteckte Dateien an.

cp [Optionen] Quelle Ziel 

    -i          Fragt den Benutzer, ob das Ziel überschrieben werden soll, falls es bereits vorhanden ist. 
    -r          Kopiert rekursiv (mit Unterverzeichnissen).

rm [Optionen] Datei(en)

    -r          Löscht auch eventuell vorhandene Unterverzeichnisse.
    -i          Fordert den Benutzer vor dem Löschen jeder einzelnen Datei zur Bestätigung auf. 

ln [Optionen] Quelle Ziel 

    -s          Erstellt eine symbolische Verknüpfung.

cd [Optionen] [Verzeichnis] 

    /           zum Root Verzeichnis Wechseln

cat [Optionen] Datei(en) 

    -n          Nummeriert die Ausgabe am linken Rand.

mv [Optionen] Quelle Ziel 

    -b          Erstellt vor dem Verschieben eine Sicherungskopie der Quelle.
    -i          Fragt den Benutzer, ob das Ziel überschrieben werden soll, falls es bereits vorhanden ist.
    
---

## Navigationsbefehl

`cd /home/`   zum Pfad /home/ navigieren (change directory)

`pwd`         aktuelles Arbeitsverzeichnis ausgeben (print working directory)

`cd`          zum Heimatverzeichnis (Standardmäßig /home/benutzername/ wechseln

`cd -`        zum letzen Verzeichnis wechseln

`pushd .`    aktuellen Pfad zwischenspeichern

`popd`        zum zwischengespeicherten Pfad wechseln

---

## Benutzer und Gruppen verwalten
`sudo`        Einen Befehl als admin ausführen

`su`          Als Admin anmelden, oder SU + Benutzername den Benutzer wechseln

`useradd`     Einen Benutzer anlegen

`userdel`     Einen Benutzer löschen

`usermod`     Einen Benutzer ändern

`groupadd`    Eine Benutzergruppe anlegen

`groupdel`    Eine Benutzergruppe löschen

`groupmod`    Eine Benutzergruppe ändern

`passwd`      Passwort einen Benutzers ändern

`chfn`        Informationen eine Users bearbeiten

`id`          Anzeige der Benutzer ID und Gruppen ID (Kennung)

`last`        Die letzten logins nach Datum und Uhrzeit anzeigen

`login`       Benutzer (neu)anmelden

`who`         Die aktuell auf dem System eingeloggten User anzeigen

`whoami`      Anzeige des Benutzer mit dem gerade gearbeitet wird

`id`          Ermitteln der effektiven UIDs und GIDs

`groups`      Die Gruppenzugehörigkeit ermitteln 

---

## Benutzer und Gruppe Rechte

`ls -la`      Anzeigen von Datei- und Verzeichniseigenschaften

`chmod`       Ändern der Dateizugriffsrechte

`chown`       Ändern des Eigentümers und der Gruppenzugehörigkeit von Dateien und Verzeichnisse 

`chgrp`       Ändern der Gruppenzugehörigkeit von Dateien oder Verzeichnissen

#### Beispiel

```ls -la /var/mail/
drwxrwsr-x 2 root mail 4,0K Apr 23  2012 /var/mail/```

Der erste Buchstabe kennzeichnet den Dateityp. Danach folgen die Zugriffsrechte.

root ist Eigentümer der Datei

mail ist die Gruppe

### Mögliche Werte
                                    Numerisch   Symbolisch
                                    
Lesen, schreiben und ausführen          7           rwx

Lesen und Schreiben                         	6 	 	   rw-
    
Lesen und Ausführen                         	5 	 	   r-x 

Nur lesen 	                            4    	   r-- 

Schreiben und Ausführen 	            3 	 	   -wx 

Nur Schreiben                        	2 		   -w-	

Nur Ausführen 	                        1 	 	   --x	

Keine Rechte 	                        0 	 	   ---                                    
 
---

## Datei Management

`cat datei.txt`           Inhalt von datei.txt direkt ausgeben

`more datei.txt`          Datei Seitenweise ausgeben, Navigieren mit Pfeiltasten, Leertaste für nächste Seite.

`less datei.txt`          wie more, jedoch mehr Funktionen (siehe manpage: man less). q zum beenden

`lspci | less`            Ausgabe von lspci an less weiterleiten

`tail datei.txt`          Die letzten Zeilen von datei.txt ausgeben

`tail -f datei.txt`       Die letzten Zeilen von datei.txt ausgeben und auf Änderungen warten. Wird der Datei etwas hinzugefügt, wird es direkt ausgegeben. Beenden mit STRG + C. Nützlich vor allem für Logdateien

`nano datei.txt`          öffnet datei.txt in nano, ein einfaches Textbearbeitungsprogramm. Zum beenden STRG+X

`vi oder vim datei.txt`   öffnet datei.txt in vi, ein sehr umfangreiches Textbearbeitungsprogramm. Zum Beenden ESC q! ENTER. Unbedingt manpage vor dem benutzen lesen!

`sort datei.txt`          gibt datei.txt sortiert aus

`rename`                  Umbenennung von Dateien 

`cut`                     Spaltenweise Manipulation von Textdaten 

---

## Disk Management

`df`          Ausgabe des Speicherplatzes aller eingehängten Laufwerke ("disk free") 

`du`          Ausgabe des Speicherverbrauchs von Verzeichnissen ("disk usage") 

`free`        Dieser Befehl zeigt den gesamten und den belegten Arbeits- und Swap-Speicher an

`fdisk`       fdisk legt MBR-Partititonen an, löscht, manipuliert oder listet sie

`mount`       Mit diesem Befehl können Sie jeden Datenträger wie Festplatten, CD-ROM-Laufwerke und andere Laufwerke in ein Verzeichnis des Linux-Dateisystems einbinden

`umoun`t      Mit diesem Befehl hängen Sie ein gemountetes Laufwerk aus dem Dateisystem aus. Dies bezeichnet man auch als „Unmounten“

### Beispiel

df [Optionen] [Verzeichnis]

    -h          Zeigt die Anzahl der belegten Blöcke in menschenlesbarer Form in Giga-, Mega- oder Kilobyte an.
    -T          Gibt den Dateisystemtyp an (z. B. ext2 oder nfs

du [Optionen] [Pfad]

     -a         Gibt die Größe jeder einzelnen Datei an.
     -h         Zeigt die Ausgabe in menschenlesbarer Form an.
     -s         Zeigt nur die errechnete Gesamtgröße an.
     
free [Optionen]

    -b          Gibt die Werte in Byte an.
    -k          Gibt die Werte in Kilobyte an.
    -m          Gibt die Werte in Megabyte an.

mount [Optionen] [Laufwerk] Mountpunkt 

  -r             Mountet das Laufwerk mit Schreibschutz.
  -t Dateisystem Gibt das Dateisystem an. Die gebräuchlichsten sind ext2 für Linux-Festplatten, msdos für MS-DOS-Medien, vfat für das Windows-Dateisystem und iso9660 für CDs.
  
---

## Archivierung / ZIP
`tar cf archiv.tar ordner/`       ordner im aktuellen Verzeichnis in die Datei archiv.tar packen

`tar xf archiv.tar`               archiv.tar entpacken

`tar cfz a.tar.gz o/`             Archiv a.tar.gz aus Ordner o/ mit gzip komprimieren

`tar cfj a.tar.bz o/`             Archiv a.tar.bz aus Ordner o/ mit bzip komprimieren

`zip archiv.zip *`                Alle Dateien & Ordner im aktuellen Verzeichnis in archiv.zip speichern

`unzip archiv.zip`                archiv.zip entpacken

`gzip -d [Parameter] Datei(en)`   Dieser Befehl komprimiert den Inhalt von Dateien mit komplexen mathematischen Algorithmen. Die komprimierten Dateien erhalten die Erweiterung .gz und müssen vor einer erneuten Verwendung dekomprimiert werden

---

## Prozesse

`top`                 Dieser Befehl gibt einen schnellen Überblick über die laufenden Prozesse. Mit H öffnen Sie eine Seite mit kurzen Erläuterungen zu den wichtigsten Optionen dieses Programms.

`ps aux`              Ohne Angabe von Optionen zeigt dieser Befehl eine Tabelle der von Ihnen gestarteten Programme und Prozesse an. aux Zeigt eine detaillierte Liste aller Prozesse unabhängig von ihren Eigentümern an.


`kill -9 Prozess-ID`  Prozess-ID  Sendet statt des TERM-Signals ein KILL-Signal, mit dem sich nahezu jeder Prozess beenden lässt.

`killall`             Dieser Befehl entspricht dem Befehl kill, akzeptiert aber statt der Prozess-ID den Prozessnamen als Argument. Der Befehl beendet alle Prozesse mit dem angegebenen Namen. 

---

## Network Utilities

### SSH / Tunneling

SSH steht für Secure Shell und meint ein Protokoll und dazugehörige Programme, um sich über das Netzwerk auf einem Sicheren Kanal auf der Konsole eines anderen Rechners zu verbinden. Mit SSH können außerdem Sichere Tunnel für andere Protokolle erstellt werden.

#### Beispiel

`ssh hostname`                                        verbindet zur Konsole des Rechners hostname (alternativ kann auch die IP-Adresse angegeben werden)

`ssh user@hostname`                                   verbindet sich als Benutzer user
            
`ssh -L 90:localhost:80 hostname`                     leitet Port 80 von Rechner hostname auf den lokalen Port 90′weiter. In diesem Beispiel wird der Webserver (Port 80) von hostname lokal über Port 90 erreichbar (http://localhost:90).Alle Daten werden dabei verschlüsselt übertragen

`ssh -R 5901:localhost:5900 hostname                  Leitet den Lokalen Port 5900 (VNC) über einen sicheren SSH-Kanal auf den Rechner hostname weiter. hostname kann jetzt eine verschlüsselte VNC-Verbindung auf den lokalen Rechner über seinen Port 5901 herstellen. Dies ist auch sinnvoll, wenn Port 5900 durch eine Firewall gesperrt wird, der Datenverkehr läuft bei einem Tunnel immer über den SSH-Port 22!

`scp lokal.txt benutzer@hostname:/home/kopie.txt`     Kopiert die lokale Datei lokal.txt auf den entfernten Rechnerhostname in das Verzeichnis /home/ unter dem Namen kopie.txt.

`scp benutzer@hostname:/home/kopie.txt`               Kopiert die entfernte Datei /home/kopie.txt von hostname auf den Lokalen Rechner ins aktuelle Verzeichnis

---

### wget

Wget ist ein freies Kommandozeilenprogramm des GNU-Projekts zum Herunterladen von Dateien aus dem Internet.

### Beispiel

`wget http://palita.net/empty.txt            Datei empty.txt von palita.net herunterladen und im aktuellen Verzeichnis abspeichern``

`wget -c http://palita.net/empty.txt         Vorher abgebrochenen Download fortsetzen (-continue)`

---

### Bash History

`CTRL-p`          Fetch the previous command from the history list.

`CTRL-n`         Fetch the next command from the history list.

`CTRL-r`          Search history backward (incremental search).

`CTRL-s`          Search history forward (incremental search).

`Meta-p`         Search backward using non-incremental search.

`Meta-n`          Search forward using non-incremental search.

`Meta-<`          Move to the first line in the history.

`Meta->`          Move to the end of the history list.

---







    
