## PuTTY Installation

PuTTY ist ein SSH Client für Windows und Unix Plattformen wie Linux. Mit PuTTY können Sie sich von einem Windows System aus auf einem Linux System per SSH einloggen. Dieser Artikel zeigt mit einigen Screenshots, wie PuTTY funktioniert.
PuTTY kann von folgender Webseite bezogen werden: https://www.putty.org/

### SSH-Schlüsselpaar erzeugen mit PuTTY

1. Starten Sie das PuTTY-Hilfsprogramm PuTTYgen. Es öffnet sich das Hauptfenster des PuTTY Key Generators.

![alt text](https://www.lancom-systems.de/docs/LCOS/referenzhandbuch/topics/pictures/puttygen_main.png)

2. Wählen Sie die Art des zu erzeugenden Schlüssels (hier: SSH-2-RSA) und dessen Bit-Stärke (z. B. 4096). Klicken Sie dann auf Generate, um mit der Schlüsselerzeugung zu beginnen. 

3. Bewegen Sie die Maus daher solange willkürlich im Programmfenster, bis der Forschrittsbalken das Ende erreicht hat. PuTTYgen generiert die für die Schlüsselerzeugung notwendigen Zufallszahlen aus den Bewegungen des Mauszeigers, die Sie innerhalb des Programmfensters vollziehen. Nach Abschluss der Erzeugung zeigt Ihnen das Programm die erzeugten Schlüsseldaten im Hauptfenster an.

![alt text](https://www.lancom-systems.de/docs/LCOS/referenzhandbuch/topics/pictures/puttygen_keygeneration.png)

4.PuTTYgen generiert die für die Schlüsselerzeugung notwendigen Zufallszahlen aus den Bewegungen des Mauszeigers, die Sie innerhalb des Programmfensters vollziehen. Bewegen Sie die Maus daher solange willkürlich im Programmfenster, bis der Forschrittsbalken das Ende erreicht hat.

![alt text](https://www.lancom-systems.de/docs/LCOS/referenzhandbuch/topics/pictures/puttygen_finalkey.png)

5.Optional: Sofern Sie Ihren Private-Key mit einer zusätzlichen Passphrase absichern möchten, tragen Sie diese im Feld Key passphrase ein und bestätigen die Eingabe im Feld darunter.
Bitte beachten Sie, dass einige SSH-Clients das Speichern einer Passphrase nicht oder nur für die aktuelle Sitzung erlauben (PuTTY z. B. nur über Pageant). Es kann daher sinnvoll sein, auf die Eingabe einer Passphrase zu verzichten, sofern Sie diese beim Verbindungsaufbau nicht manuell eingeben wollen. LANconfig selbst unterstützt das persistente Speichern einer Passphrase.

6.Klicken Sie auf die Schaltflächen Save public key und Save private key, um Ihren öffentlichen und Ihren privaten Schlüssel zu speichern.
Den so erstellten öffentlichen Schlüssel hinterlegen Sie nach anschließender Bearbeitung im Gerät; den privaten Schlüssel verwenden Sie in Kombination mit PutTTY für die Authentisierung.

7.Wählen Sie außerdem Conversions > Export OpenSSH key, um den Schlüssel gleichzeitig als OpenSSH Private-Key abzuspeichern.
Den so erstellten privaten Schlüssel verwenden Sie in Kombination mit LANconfig für die Authentisierung.

### Login auf einem Linux System per SSH 

1.PuTTY starten und IP Adresse des Linux Systems eingeben: 

![alt text](https://www.thomas-krenn.com/de/wikiDE/images/thumb/3/35/Putty-1.png/300px-Putty-1.png)

2.Bei der ersten Verbindung muss der Key bestätigt werden: 

![alt text](https://www.thomas-krenn.com/de/wikiDE/images/thumb/4/46/Putty-2.png/300px-Putty-2.png)

3.Wählen Sie den Benutzernamen, mit dem Sie sich verbinden möchten: 

![alt text](https://www.thomas-krenn.com/de/wikiDE/images/thumb/7/7f/Putty-3.png/300px-Putty-3.png)

4.Geben Sie das Passwort ein:

![alt text](https://www.thomas-krenn.com/de/wikiDE/images/thumb/8/87/Putty-4.png/300px-Putty-4.png)

5.Daraufhin erscheint die Login Shell: 

![alt text](https://www.thomas-krenn.com/de/wikiDE/images/thumb/4/47/Putty-5.png/300px-Putty-5.png)
