# main.py (Liegt direkt im Ordner /Lernspiel)
from src.Unterlagen import Unterlagen

def main():
    print("=== Lernspiel App gestartet ===")
    
    # 1. Repository instanziieren (startet intern die DB-Schicht)
    unterlagen_repo = Unterlagen()
    
    unterlagen_repo.show_single_file()
   

if __name__ == "__main__":
    main()
