# Ordnern

### `Get-ChildItem (alias: ls, dir)`: Listet den Inhalt eines Ordners auf, einschließlich Dateien und Unterordner.

**Parameter:**

-`Recurse`: Durchsucht alle Unterverzeichnisse.

-`Directory`: Zeigt nur Ordner an.

-`Filter`: Filtert nach bestimmten Namen oder Erweiterungen.

### `New-Item`: Erstellt einen neue datei

**Parameter:**

-`Path`: Der Pfad, an dem der Ordner erstellt wird.

-`Name`: Der Name des neuen Ordners.

-`ItemType Directory`: Gibt an, dass ein Ordner erstellt werden soll

### `Copy-Item`:   Kopiert einen Ordner von einem Ort zu einem anderen.

**Parameter:**

-`Recurse`: Kopiert den Ordner und alle Unterordner.

-`Force`: Überschreibt vorhandene Dateien oder Ordner.

### `Move-Item`: Verschiebt einen Ordner an einen neuen Ort.

### `Remove-Item`: Löscht einen Ordner und seinen Inhalt.

**Parameter:**

-`Recurse`: Löscht den Ordner einschließlich aller Unterordner.
-`Force`: Erzwingt das Löschen (auch wenn der Ordner schreibgeschützt ist).