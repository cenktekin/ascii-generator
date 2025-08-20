#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Türkçe Destekli Renkli ASCII Art Generator
Kullanıcının girdiği metni renkli ASCII sanatı olarak ekrana yazdırır.
"""

import random
import os

# ANSI Renk Kodları
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Ana renkler
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Arka plan renkleri
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN = '\033[106m'
    
    # Gradient renkler
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;205m'
    PURPLE = '\033[38;5;129m'
    LIME = '\033[38;5;154m'
    GOLD = '\033[38;5;220m'

# Renk temaları
COLOR_THEMES = {
    '1': {
        'name': '🌈 Gökkuşağı',
        'colors': [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    },
    '2': {
        'name': '🔥 Ateş',
        'colors': [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GOLD]
    },
    '3': {
        'name': '🌊 Okyanus',
        'colors': [Colors.BLUE, Colors.CYAN, Colors.LIME]
    },
    '4': {
        'name': '🌸 Pembe Dünya',
        'colors': [Colors.PINK, Colors.MAGENTA, Colors.PURPLE]
    },
    '5': {
        'name': '🌿 Doğa',
        'colors': [Colors.GREEN, Colors.LIME, Colors.YELLOW]
    },
    '6': {
        'name': '⭐ Altın',
        'colors': [Colors.GOLD, Colors.YELLOW, Colors.ORANGE]
    },
    '7': {
        'name': '🎭 Rastgele',
        'colors': [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN, Colors.ORANGE, Colors.PINK]
    }
}

# ASCII karakter haritası - her karakter 5x3 boyutunda
ASCII_MAP = {
    'a': [
        " ███ ",
        "█   █",
        "█████",
        "█   █",
        "█   █"
    ],
    'b': [
        "████ ",
        "█   █",
        "████ ",
        "█   █",
        "████ "
    ],
    'c': [
        " ███ ",
        "█    ",
        "█    ",
        "█    ",
        " ███ "
    ],
    'd': [
        "████ ",
        "█   █",
        "█   █",
        "█   █",
        "████ "
    ],
    'e': [
        "█████",
        "█    ",
        "████ ",
        "█    ",
        "█████"
    ],
    'f': [
        "█████",
        "█    ",
        "████ ",
        "█    ",
        "█    "
    ],
    'g': [
        " ███ ",
        "█    ",
        "█ ██ ",
        "█   █",
        " ███ "
    ],
    'h': [
        "█   █",
        "█   █",
        "█████",
        "█   █",
        "█   █"
    ],
    'i': [
        "█████",
        "  █  ",
        "  █  ",
        "  █  ",
        "█████"
    ],
    'j': [
        "█████",
        "    █",
        "    █",
        "█   █",
        " ███ "
    ],
    'k': [
        "█   █",
        "█  █ ",
        "███  ",
        "█  █ ",
        "█   █"
    ],
    'l': [
        "█    ",
        "█    ",
        "█    ",
        "█    ",
        "█████"
    ],
    'm': [
        "█   █",
        "██ ██",
        "█ █ █",
        "█   █",
        "█   █"
    ],
    'n': [
        "█   █",
        "██  █",
        "█ █ █",
        "█  ██",
        "█   █"
    ],
    'o': [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    'p': [
        "████ ",
        "█   █",
        "████ ",
        "█    ",
        "█    "
    ],
    'q': [
        " ███ ",
        "█   █",
        "█   █",
        "█  ██",
        " ████"
    ],
    'r': [
        "████ ",
        "█   █",
        "████ ",
        "█  █ ",
        "█   █"
    ],
    's': [
        " ███ ",
        "█    ",
        " ███ ",
        "    █",
        " ███ "
    ],
    't': [
        "█████",
        "  █  ",
        "  █  ",
        "  █  ",
        "  █  "
    ],
    'u': [
        "█   █",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    'v': [
        "█   █",
        "█   █",
        "█   █",
        " █ █ ",
        "  █  "
    ],
    'w': [
        "█   █",
        "█   █",
        "█ █ █",
        "██ ██",
        "█   █"
    ],
    'x': [
        "█   █",
        " █ █ ",
        "  █  ",
        " █ █ ",
        "█   █"
    ],
    'y': [
        "█   █",
        " █ █ ",
        "  █  ",
        "  █  ",
        "  █  "
    ],
    'z': [
        "█████",
        "   █ ",
        "  █  ",
        " █   ",
        "█████"
    ],
    # Türkçe karakterler
    'ç': [
        " ███ ",
        "█    ",
        "█    ",
        "█    ",
        " ███ ",
    ],
    'ş': [
        " ███ ",
        "█    ",
        " ███ ",
        "    █",
        " ███ "
    ],
    'ı': [
        "     ",
        "  █  ",
        "  █  ",
        "  █  ",
        "  █  "
    ],
    'ğ': [
        " ▄▄  ",
        " ███ ",
        "█    ",
        "█ ██ ",
        " ███ "
    ],
    'ö': [
        " ▄ ▄ ",
        " ███ ",
        "█   █",
        "█   █",
        " ███ "
    ],
    'ü': [
        " ▄ ▄ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    # Rakamlar
    '0': [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    '1': [
        "  █  ",
        " ██  ",
        "  █  ",
        "  █  ",
        "█████"
    ],
    '2': [
        " ███ ",
        "█   █",
        "   █ ",
        " █   ",
        "█████"
    ],
    '3': [
        " ███ ",
        "    █",
        " ███ ",
        "    █",
        " ███ "
    ],
    '4': [
        "█   █",
        "█   █",
        "█████",
        "    █",
        "    █"
    ],
    '5': [
        "█████",
        "█    ",
        "████ ",
        "    █",
        "████ "
    ],
    '6': [
        " ███ ",
        "█    ",
        "████ ",
        "█   █",
        " ███ "
    ],
    '7': [
        "█████",
        "    █",
        "   █ ",
        "  █  ",
        " █   "
    ],
    '8': [
        " ███ ",
        "█   █",
        " ███ ",
        "█   █",
        " ███ "
    ],
    '9': [
        " ███ ",
        "█   █",
        " ████",
        "    █",
        " ███ "
    ],
    # Boşluk ve özel karakterler
    ' ': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ],
    '?': [
        " ███ ",
        "█   █",
        "   █ ",
        "     ",
        "  █  "
    ],
    '!': [
        "  █  ",
        "  █  ",
        "  █  ",
        "     ",
        "  █  "
    ],
    '.': [
        "     ",
        "     ",
        "     ",
        "     ",
        "  █  "
    ],
    ',': [
        "     ",
        "     ",
        "     ",
        "  █  ",
        " █   "
    ]
}

def clear_screen():
    """Ekranı temizler."""
    os.system('clear' if os.name == 'posix' else 'cls')

def show_color_menu():
    """Renk seçeneklerini gösterir."""
    print(f"{Colors.BOLD}{Colors.CYAN}🎨 RENK SEÇENEKLERI:{Colors.RESET}")
    print("=" * 40)
    
    for key, theme in COLOR_THEMES.items():
        colors_preview = ""
        for color in theme['colors'][:3]:  # İlk 3 rengi göster
            colors_preview += f"{color}█{Colors.RESET}"
        print(f"{key}. {theme['name']} {colors_preview}")
    
    print("=" * 40)
    
    while True:
        choice = input("Renk teması seçin (1-7): ").strip()
        if choice in COLOR_THEMES:
            return COLOR_THEMES[choice]['colors']
        print(f"{Colors.RED}Geçersiz seçim! Lütfen 1-7 arası bir sayı girin.{Colors.RESET}")

def get_user_input():
    """Kullanıcıdan metin girişi alır ve doğrular."""
    while True:
        try:
            text = input(f"{Colors.BOLD}ASCII sanatı için metin girin (max 20 karakter): {Colors.RESET}").strip()
            
            if len(text) == 0:
                print(f"{Colors.RED}Lütfen en az bir karakter girin!{Colors.RESET}")
                continue
            
            if len(text) > 20:
                print(f"{Colors.RED}Metin çok uzun! ({len(text)} karakter). Maksimum 20 karakter olmalı.{Colors.RESET}")
                continue
            
            return text.lower()
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Çıkılıyor...{Colors.RESET}")
            exit(0)
        except Exception as e:
            print(f"{Colors.RED}Bir hata oluştu: {e}{Colors.RESET}")

def text_to_ascii_art(text, colors):
    """Metni renkli ASCII sanatına dönüştürür."""
    if not text:
        return []
    
    # Her karakterin ASCII temsilini al
    char_patterns = []
    char_colors = []
    
    for i, char in enumerate(text):
        if char in ASCII_MAP:
            char_patterns.append(ASCII_MAP[char])
        else:
            # Desteklenmeyen karakter için placeholder kullan
            char_patterns.append(ASCII_MAP['?'])
        
        # Her karakter için renk seç
        if len(colors) == 1:
            char_colors.append(colors[0])
        else:
            char_colors.append(colors[i % len(colors)])
    
    # ASCII sanatı satırlarını oluştur
    ascii_lines = []
    for row in range(5):  # Her karakter 5 satır yüksekliğinde
        line = ""
        for i, pattern in enumerate(char_patterns):
            colored_pattern = f"{char_colors[i]}{pattern[row]}{Colors.RESET}"
            line += colored_pattern + " "  # Karakterler arası boşluk
        ascii_lines.append(line.rstrip())  # Sondaki boşlukları temizle
    
    return ascii_lines

def print_ascii_art(ascii_lines, text):
    """Renkli ASCII sanatını ekrana yazdırır."""
    border = f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}"
    
    print("\n" + border)
    print(f"{Colors.BOLD}{Colors.GOLD}🎨 ASCII SANAT ÇIKTISI: '{text.upper()}' 🎨{Colors.RESET}")
    print(border)
    print()
    
    for line in ascii_lines:
        print(f"  {line}")
    
    print()
    print(border + "\n")

def main():
    """Ana program fonksiyonu."""
    clear_screen()
    
    # Başlık
    print(f"{Colors.BOLD}{Colors.GOLD}🎨 TÜRKÇE DESTEKLİ RENKLİ ASCII ART GENERATOR 🎨{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.GREEN}✨ Türkçe karakterler desteklenir: ç, ş, ı, ğ, ö, ü{Colors.RESET}")
    print(f"{Colors.BLUE}📝 Maksimum 20 karakter girebilirsiniz.{Colors.RESET}")
    print(f"{Colors.MAGENTA}🌈 Renkli çıktı ile güzel görünüm!{Colors.RESET}")
    print(f"{Colors.RED}❌ Çıkmak için Ctrl+C tuşlayın.{Colors.RESET}\n")
    
    while True:
        try:
            # Renk teması seç
            selected_colors = show_color_menu()
            print()
            
            # Kullanıcıdan metin al
            user_text = get_user_input()
            
            # ASCII sanatına dönüştür
            ascii_art = text_to_ascii_art(user_text, selected_colors)
            
            # Ekrana yazdır
            print_ascii_art(ascii_art, user_text)
            
            # Devam etmek isteyip istemediğini sor
            continue_choice = input(f"{Colors.BOLD}Başka bir metin denemek ister misiniz? (e/h): {Colors.RESET}").lower()
            if continue_choice not in ['e', 'evet', 'y', 'yes']:
                print(f"{Colors.GOLD}Güle güle! 👋✨{Colors.RESET}")
                break
            
            print("\n" + "-"*60 + "\n")
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.GOLD}Güle güle! 👋✨{Colors.RESET}")
            break
        except Exception as e:
            print(f"{Colors.RED}Beklenmeyen bir hata oluştu: {e}{Colors.RESET}")

if __name__ == "__main__":
    main()
