# PowerShell Cheat Sheet

## Grundlegende Befehle

-`Get-Help`: Zeigt Hilfeinformationen zu einem Befehl an.

-`Get-Command`: Zeigt alle verfügbaren PowerShell-Befehle oder Informationen zu einem bestimmten Befehl an.


## Ordnern/Dateen

### `Get-ChildItem (alias: ls, dir)`: Listet Dateien/Ordern und Verzeichnisse in einem angegebenen Pfad auf.

**Parameter:**

-`Recurse`: Durchsucht alle Unterverzeichnisse.

-`Directory`: Zeigt nur Ordner an.

-`Filter`: Filtert nach bestimmten Namen oder Erweiterungen.

### `New-Item` / `mkdir`: Erstellt eine neue Datei oder ein neues Verzeichnis.

**Parameter:**

-`Path`: Der Pfad, an dem der Ordner erstellt wird.

-`Name`: Der Name des neuen Ordners.

-`ItemType Directory`: Gibt an, dass ein Ordner erstellt werden soll

### `Copy-Item`:   Kopiert eine Datei oder ein Verzeichnis.

**Parameter:**

-`Recurse`: Kopiert den Ordner und alle Unterordner.

-`Force`: Überschreibt vorhandene Dateien oder Ordner.

### `Move-Item`: Verschiebt eine Datei oder ein Verzeichnis.

### `Remove-Item`: Löscht eine Datei oder ein Verzeichnis.

**Parameter:**

-`Recurse`: Löscht den Ordner einschließlich aller Unterordner.
-`Force`: Erzwingt das Löschen (auch wenn der Ordner schreibgeschützt ist).

### `Rename-Item`: Ändert den Namen eines Ordners.
### `Get-Item`: Zeigt Informationen zu einem bestimmten Ordner an.

### `Expand-Archive`: Entpackt eine ZIP-Datei in einen Ordner.

# Informationen über das System

### `Get-Service`: Listet alle Dienste auf dem System auf.

### `Get-EventLog`: Liest Einträge aus einem Windows-Eventlog.

### `Get-WmiObject`: Greift auf WMI-Objekte (Windows Management Instrumentation) zu.