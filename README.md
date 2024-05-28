# ZabezpieczPDF

ZabezpieczPDF to narzędzie do zabezpieczania plików PDF hasłem. Program pozwala na wygenerowanie losowego hasła lub wprowadzenie własnego hasła, a następnie zabezpiecza wszystkie pliki PDF w bieżącym katalogu.

## Autor

Michał Kowalski  
[www.cyberbezpiecznysamorzad.plus](http://www.cyberbezpiecznysamorzad.plus)  
kontakt@cyberbezpiecznysamorzad.plus  
tel. 606-576-299

## Wersja

0.0.1

## Wymagania

- Python 3.x
- Biblioteki: `PyPDF2`, `pyperclip`, `PyInstaller`

## Instalacja

1. **Klonowanie repozytorium:**

    ```sh
    git clone https://github.com/ozoadmin/zabezpieczpdf.git
    cd zabezpieczpdf
    ```

2. **Instalacja wymaganych bibliotek:**

    ```sh
    pip install PyPDF2 pyperclip pyinstaller
    ```

## Użycie

1. **Uruchomienie programu:**

    ```sh
    python ZabezpieczPDF.py
    ```

2. **Konwersja skryptu na plik EXE:**

    Aby przekonwertować skrypt na plik EXE, użyj `PyInstaller`:

    ```sh
    pyinstaller --onefile ZabezpieczPDF.py
    ```

    Po wykonaniu tego polecenia, w folderze `dist` znajdziesz plik `ZabezpieczPDF.exe`, który możesz uruchomić, aby zabezpieczyć pliki PDF w bieżącym katalogu za pomocą okien wiersza poleceń.

## Funkcje

- **Generowanie losowego hasła:** Program może wygenerować losowe hasło spełniające wymagania dotyczące złożoności hasła.
- **Walidacja własnego hasła:** Użytkownik może wprowadzić własne hasło, które musi spełniać określone wymagania.
- **Kopiowanie hasła do schowka:** Wygenerowane hasło jest kopiowane do schowka.
- **Zabezpieczanie plików PDF:** Program zabezpiecza wszystkie pliki PDF w bieżącym katalogu przy użyciu szyfrowania AES-128.
- **Interaktywny interfejs wiersza poleceń:** Program wyświetla komunikaty i instrukcje w interfejsie wiersza poleceń.

## Przykładowe użycie

1. **Po uruchomieniu programu:**

    ```
    =======================================================
    Program: ZabezpieczPDF
    Autor: Michał Kowalski | www.cyberbezpiecznysamorzad.plus | kontakt@cyberbezpiecznysamorzad.plus | tel. 606-576-299
    Wersja: 0.0.1
    =======================================================
    ```

2. **Generowanie losowego hasła:**

    ```
    Sugerowane hasło: Ab1!xyZ2
    Jeśli akceptujesz sugerowane hasło, naciśnij Enter.
    -------------------------------------------------------
    Jeśli chcesz użyć własnego hasła, wprowadź je poniżej zgodnie z wymaganiami:
    - Min. 8 znaków
    - Przynajmniej jedna wielka litera
    - Przynajmniej jedna mała litera
    - Przynajmniej jedna cyfra
    - Przynajmniej jeden znak specjalny
    -------------------------------------------------------
    ```

3. **Zabezpieczanie plików PDF:**

    ```
    -------------------------------------------------------
    Zabezpieczanie plików PDF zakończone.
    Pliki zostały zabezpieczone przy użyciu szyfrowania AES-128.
    -------------------------------------------------------
    ```

4. **Odliczanie przed zamknięciem programu:**

    ```
    Program zamknie się za 3 sekund...
    Program zamknie się za 2 sekund...
    Program zamknie się za 1 sekund...
    ```

## Licencja

Ten projekt jest licencjonowany na zasadach MIT License.
