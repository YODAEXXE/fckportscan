import sys
import time
import os
import random

try:
    import pyfiglet
    BANNER = pyfiglet.figlet_format("fckportscan", font="doom")
except ImportError:
    BANNER = r"""
  __     _                     _                       
 / _|   | |                   | |                      
| |_ ___| | ___ __   ___  _ __| |_ ___  ___ __ _ _ __  
|  _/ __| |/ / '_ \ / _ \| '__| __/ __|/ __/ _` | '_ \ 
| || (__|   <| |_) | (_) | |  | |_\__ \ (_| (_| | | | |
|_| \___|_|\_\ .__/ \___/|_|   \__|___/\___\__,_|_| |_|
             | |                                       
             |_|                                       
"""

# Paleta roxa
PURPLE = ["35", "95", "35", "95", "35", "95", "35", "95"]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def color(code, text):
    return f"\033[{code}m{text}\033[0m"

def glitch_banner():
    """Efeito glitch com interferência antes de estabilizar."""
    chars = list("!@#$%^&*-=+?/\\|~<>")
    lines = BANNER.strip('\n').split('\n')
    for _ in range(10):
        clear()
        glitched = []
        for line in lines:
            new_line = ""
            for ch in line:
                if ch not in (' ', '\n') and random.random() > 0.6:
                    new_line += random.choice(chars)
                else:
                    new_line += ch
            glitched.append(new_line)
        c = random.choice(PURPLE)
        print(color(c, '\n'.join(glitched)))
        time.sleep(0.06)

def purple_banner():
    """Exibe o banner com degradê roxo linha por linha."""
    clear()
    lines = BANNER.strip('\n').split('\n')
    for i, line in enumerate(lines):
        c = PURPLE[i % len(PURPLE)]
        print(color(c, line))
        time.sleep(0.07)

def typewriter_banner():
    """Digita o banner letra por letra em roxo."""
    clear()
    sys.stdout.write("\033[95m")
    for ch in BANNER:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch not in (' ', '\n'):
            time.sleep(0.003)
    sys.stdout.write("\033[0m")

def scan_banner():
    """Revela o banner linha por linha como varredura roxa."""
    clear()
    lines = BANNER.strip('\n').split('\n')
    for i in range(len(lines) + 1):
        clear()
        for line in lines[:i]:
            print(color("95", line))
        for line in lines[i:]:
            print(color("90", '░' * len(line)))
        time.sleep(0.09)

def show_banner(mode="glitch"):
    """
    Animação do banner fckportscan em roxo.

    Modos:
      'glitch'      — interferência com chars aleatórios + roxo
      'typewriter'  — digita letra por letra em roxo
      'purple'      — cada linha em tom de roxo alternado
      'scan'        — revela o banner como varredura roxa
    """
    if mode == "glitch":
        glitch_banner()
        purple_banner()
    elif mode == "typewriter":
        typewriter_banner()
    elif mode == "purple":
        purple_banner()
    elif mode == "scan":
        scan_banner()

    print()
    print(color("90", "  " + "─" * 54))
    print(color("95", "  [*] by fckmott | Wi-Fi & Network Recon Tool"))
    print(color("90", "  " + "─" * 54))
    print()
    time.sleep(0.3)


# ── Teste direto ──────────────────────────────────────────
if __name__ == "__main__":
    show_banner(mode="glitch")
    print(color("95", "  Scanner pronto. Iniciando..."))
    time.sleep(1)
