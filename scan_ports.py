"""
scan_ports.py
--------------
Scanner de ports défensif — Cyberanalyste-Défensif

Objectif pédagogique :
Ce script vérifie quels ports sont ouverts sur UNE adresse IP que TU contrôles
(ton propre ordinateur, un appareil de ton réseau local, etc.).

⚠️ IMPORTANT — Usage légal et éthique :
Scanner une adresse IP qui ne t'appartient pas, ou sans autorisation explicite
du propriétaire, peut être ILLÉGAL, même à but éducatif.
Utilise ce script uniquement sur :
  - Ton propre ordinateur (127.0.0.1 / localhost)
  - Un appareil de ton réseau local que tu possèdes ou administres
  - Un système pour lequel tu as une permission écrite

Pourquoi scanner ses propres ports ?
Un port ouvert = une porte d'entrée potentielle vers ton appareil.
Savoir lesquels sont ouverts permet de fermer ceux qui ne sont pas nécessaires,
réduisant ainsi la surface d'attaque (principe de base en cyberdéfense).
"""

import socket
from datetime import datetime

PORTS_COURANTS = {
    21: "FTP (transfert de fichiers)",
    22: "SSH (accès à distance sécurisé)",
    23: "Telnet (accès à distance NON sécurisé)",
    25: "SMTP (envoi de courriels)",
    53: "DNS (résolution de noms de domaine)",
    80: "HTTP (site web non sécurisé)",
    110: "POP3 (réception de courriels)",
    143: "IMAP (réception de courriels)",
    443: "HTTPS (site web sécurisé)",
    445: "SMB (partage de fichiers Windows)",
    3306: "MySQL (base de données)",
    3389: "RDP (bureau à distance Windows)",
    5432: "PostgreSQL (base de données)",
    8080: "HTTP alternatif (souvent utilisé pour du développement)",
}


def scanner_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        resultat = s.connect_ex((ip, port))
        return resultat == 0


def scanner_ip(ip: str) -> None:
    print(f"\nScan de {ip} — démarré à {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    ports_ouverts = []

    for port, service in PORTS_COURANTS.items():
        if scanner_port(ip, port):
            print(f"[OUVERT]  Port {port:<5} — {service}")
            ports_ouverts.append(port)
        else:
            print(f"[fermé]   Port {port:<5} — {service}")

    print("-" * 50)
    if ports_ouverts:
        print(f"Résumé : {len(ports_ouverts)} port(s) ouvert(s) → {ports_ouverts}")
        print("Conseil : ferme les ports/services que tu n'utilises pas.")
    else:
        print("Résumé : aucun port courant ouvert détecté.")


if __name__ == "__main__":
    print("=== Scanner de ports défensif — Cyberanalyste-Défensif ===")
    print("⚠️  À utiliser uniquement sur un appareil qui t'appartient.\n")

    cible = input("Entre l'adresse IP à scanner (ex: 127.0.0.1 pour ton propre ordi) : ").strip()

    if not cible:
        print("Aucune adresse fournie. Arrêt du script.")
    else:
        scanner_ip(cible)
