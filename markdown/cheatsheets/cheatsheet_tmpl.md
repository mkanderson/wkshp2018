### <Befehl> Cheetsheat

#### Befehl Syntax
```
BEFEHL [OPTION] [VERZEICHNIS] 
```
---
#### Häufig verwendete Optionen

`-s  #snarkmode`
`-X  #XBOX audio`
`-BB #Homerun (in Baseball mode)`
---
#### Beispiele
*Spielestats extrahieren, sortieren und in Logdatei umleiten*

```
BEFEHL -Xs JoeDiMaggio | frep -ipv4 >> /var/log/fNord.log
```

---
