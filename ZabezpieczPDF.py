import os
import random
import string
import re
import time
from PyPDF2 import PdfReader, PdfWriter
import pyperclip

def generate_random_password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()"

    # Avoid similar characters
    avoid_similar = {'0', 'O', '1', 'l', 'I', '5', 'S'}

    lower = ''.join([c for c in lower if c not in avoid_similar])
    upper = ''.join([c for c in upper if c not in avoid_similar])
    digits = ''.join([c for c in digits if c not in avoid_similar])
    
    all_chars = lower + upper + digits + special
    
    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all_chars
    password += random.choices(all_chars, k=4)

    # Shuffle the list to ensure random order and convert to string
    random.shuffle(password)
    return ''.join(password)

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*()]', password):
        return False
    return True

def secure_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])

    writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Program zamknie się za {i} sekund...")
        time.sleep(1)

def main():
    # Nagłówek programu
    print("=======================================================")
    print("Program: ZabezpieczPDF")
    print("Autor: Michał Kowalski | www.cyberbezpiecznysamorzad.plus | kontakt@cyberbezpiecznysamorzad.plus | tel. 606-576-299")
    print("Wersja: 0.0.1")
    print("=======================================================")

    # Pobierz wszystkie pliki PDF w bieżącym katalogu
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("-------------------------------------------------------")
        print("Brak plików PDF w bieżącym katalogu.")
        print("-------------------------------------------------------")
        countdown(3)
        return

    # Generowanie losowego hasła
    generated_password = generate_random_password()
    print(f"Sugerowane hasło: {generated_password}")
    print("Jeśli akceptujesz sugerowane hasło, naciśnij Enter.")
    print("-------------------------------------------------------")
    print("Jeśli chcesz użyć własnego hasła, wprowadź je poniżej zgodnie z wymaganiami:")
    print("- Min. 8 znaków")
    print("- Przynajmniej jedna wielka litera")
    print("- Przynajmniej jedna mała litera")
    print("- Przynajmniej jedna cyfra")
    print("- Przynajmniej jeden znak specjalny")
    print("-------------------------------------------------------")

    user_input = input("Podaj hasło do zabezpieczenia plików PDF (lub naciśnij Enter, aby użyć sugerowanego hasła): ")

    if user_input == "":
        password = generated_password
        pyperclip.copy(password)
        print("\033[91m\033[4mWygenerowane hasło zostało skopiowane do schowka.\033[0m")
    else:
        password = user_input
        while not validate_password(password):
            print("-------------------------------------------------------")
            print("Hasło nie spełnia wymagań. Spróbuj ponownie.")
            print("-------------------------------------------------------")
            password = input("Podaj hasło do zabezpieczenia plików PDF: ")
            if password == "":
                password = generated_password
                pyperclip.copy(password)
                print("\033[91m\033[4mWygenerowane hasło zostało skopiowane do schowka.\033[0m")
                break

    # Upewnij się, że istnieje katalog 'secured_pdfs'
    secured_pdfs_directory = 'secured_pdfs'
    if not os.path.exists(secured_pdfs_directory):
        os.makedirs(secured_pdfs_directory)

    for pdf_file in pdf_files:
        # Ścieżka do oryginalnego pliku PDF
        original_file_path = os.path.join('.', pdf_file)

        # Ścieżka do nowego, zabezpieczonego pliku PDF
        file_name, file_extension = os.path.splitext(pdf_file)
        secured_file_path = os.path.join(secured_pdfs_directory, f"{file_name}_secured{file_extension}")

        # Zabezpiecz plik PDF hasłem
        secure_pdf(original_file_path, secured_file_path, password)

    print("-------------------------------------------------------")
    print("Zabezpieczanie plików PDF zakończone.")
    print("Pliki zostały zabezpieczone przy użyciu szyfrowania AES-128.")
    print("-------------------------------------------------------")
    
    # Poczekaj 3 sekundy przed zamknięciem programu
    countdown(3)

if __name__ == "__main__":
    main()
