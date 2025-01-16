## Task 1 - Hadi a žebříky

Hráči, kola hry a herní pole jsou indexovány od 0.

### Spuštění hry

Hru spustíte pomocí příkazu:
```bash
python3 task1/game.py
```
v kořenovém adresáři projektu.

### Testy

Pro hru jsem vytvořil několik jednoduchých testů pro funkce `game_loop` a `player_move` za pomocí knihovny `pytest`. Testy spustíte pomocí příkazu:
```bash
uv run pytest .
```
v kořenovém adresáři projektu.

## Task 2 - OOP

### Spuštění

Program spustíte příkazem:
```bash
python3 task2/html.py
```
v kořenovém adresáři projektu.

## Task 3 - Databáze

Vytvořil jsem si Container s PostgreSQL databází. 

První je potřeba vytvořit volume pro ukládání dat:
```bash
docker volume create olc-volume
```
Vytvořil jednoduchý script `run-db`, který spustí databázi a připojí ji k vytvořenému volume. Pro první spuštění je potřeba zavolat `docker build` přidáním flagu `-b` nebo `--build`:
```bash
./run-db -b
```
Při prvním běhu je potřeba nahrát schéma databáze a data z zadaného GitHubu. Vše je pak uloženo v definovaném volume.

Jednotilivé dotazy jsou rozděleny do vlastních souborů `query1-4.sql`.

Funkce je v souboru `function.sql`, který obsahuje definici funkce, volání funkce a dotaz na danou tabulku.
