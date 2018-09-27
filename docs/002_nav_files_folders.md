
### Lab 2 > Orientierung im Unix Dateisystem, Ordner und Dateien

`prompt` `ls` `pwd` `cd` `mkdir` 

---
##### `Aufgabe` 

Nach erfolgreichem Login befinden wir uns in der Linux Shell (Bash) Umgebung:

```
Linux stan 4.9.0-7-amd64 #1 SMP Debian 4.9.110-1 (2018-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
otto@stan:~$ 
```

Auf der Eingabeaufforderung (Prompt) können wir Befehle eingeben und deren Ausgabe lesen. Eingaben werden mit der `ENTER` Taste terminiert.
 
---

#### Unix Dateisystem Hierarchy

Eine Unix Dateisystem ist hierarchisch - Verzeichnisse können ein oder mehrere Dateien oder weitere Unterverzeichnisse beinhalten:

```
.
└── files
    ├── important
    │   └── Steuer2017.pgd
    ├── stuff
    │   ├── mail
    │   ├── notes
    │   │   ├── einkaufsliste.txt
    │   │   └── schatzi.txt
    │   └── todo
    └── trash
```

Auf der Kommandozeile werden einzelne Pfadkomponente mit der '/' Zeichen getrennt. Folglich wird im obigen Beispiel die Datei "einkaufsliste.txt" als `files/stuff/notes/einkaufliste.txt` addressiert.

Das oberste Knoten der Hierarchie ist `/`, oft 'Slash' genannt. Die Standard-Struktur der Linux Dateisystem wird im [Linux Filesystem Hierarchy Standard](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) vorgeben. 


