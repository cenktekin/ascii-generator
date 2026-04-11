# -*- coding: utf-8 -*-
"""
Rich-based renderer for ASCII Art Generator.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src.assets import ASCII_SHAPES, COLOR_THEMES, NAME_TO_SHAPE

console = Console()


class Renderer:
    """Terminal renderer using Rich library."""

    @staticmethod
    def clear_screen():
        console.clear()

    @staticmethod
    def print_header():
        """Print application header."""
        title = Text("🎨 ASCII ART GENERATOR 🎨", style="bold gold1")
        subtitle = Text("Türkçe Destekli • Renkli Çıktı • Emoji Şekiller", style="cyan")

        panel = Panel(
            Text.assemble(title, "\n", subtitle), border_style="cyan", padding=(1, 2)
        )
        console.print(panel)

    @staticmethod
    def show_color_menu():
        """Display color theme selection menu."""
        table = Table(title="🎨 Renk Temaları", show_header=False, box=None)
        table.add_column("No", style="cyan bold", width=4)
        table.add_column("İsim", style="white")
        table.add_column("Önizleme", width=20)

        for key, theme in COLOR_THEMES.items():
            preview = "".join([f"{c}█[reset]" for c in theme["colors"][:4]])
            table.add_row(key, theme["name"], preview)

        console.print(table)
        return table

    @staticmethod
    def show_main_menu():
        """Display main menu and return choice."""
        table = Table(title="📋 Ana Menü", show_header=False, box=None)
        table.add_column("No", style="cyan bold", width=4)
        table.add_column("Açıklama", style="white")

        table.add_row("1", "📝 Normal ASCII (Metin → ASCII)")
        table.add_row("2", "🎭 İsim + Şekil (kedi → KEDİ + 🐱)")
        table.add_row("3", "❌ Çıkış")

        console.print(table)

        while True:
            choice = console.input("[bold cyan]Seçiminiz (1-3): [/bold cyan]")
            if choice in ["1", "2", "3"]:
                return choice
            console.print("[red]Geçersiz seçim![/red]")

    @staticmethod
    def show_supported_names():
        """Display supported shape names."""
        categories = {
            "🐾 Hayvanlar": ["kuş", "kedi", "köpek", "balık", "kelebek"],
            "🌿 Doğa": ["çiçek", "ağaç", "güneş", "ay", "yıldız"],
            "🏠 Objeler": ["kalp", "ev", "araba"],
            "💝 Duygular": ["sevgi", "aşk", "mutluluk"],
        }

        for category, names in categories.items():
            console.print(f"\n[bold]{category}:[/bold]")
            for name in names:
                console.print(f"  • {name}")

        console.print("\n[dim]💡 İngilizce karşılıklar da desteklenir[/dim]")

    @staticmethod
    def render_ascii_art(lines, text, theme_name):
        """Render ASCII art with panel."""
        if not lines:
            return

        content = "\n".join(lines)
        title = f"🎨 {text.upper()} 🎨"

        panel = Panel(content, title=title, border_style="gold1", padding=(1, 2))
        console.print(panel)

    @staticmethod
    def render_name_shape(name_ascii, shape_lines, name, shape_key):
        """Render name + shape ASCII art."""
        if name_ascii:
            console.print("\n[bold magenta]📝 İSİM:[/bold magenta]")
            for line in name_ascii:
                console.print(f"  {line}")

        if shape_lines and shape_key in ASCII_SHAPES:
            console.print(f"\n[bold green]🎨 ŞEKİL ({shape_key.upper()}):[/bold green]")
            for line in shape_lines:
                console.print(f"  {line}")
        else:
            console.print(f"\n[yellow]⚠️  '{name}' için şekil bulunamadı[/yellow]")

    @staticmethod
    def ask_continue(prompt="Devam etmek ister misiniz?"):
        """Ask user to continue."""
        response = console.input(f"[bold]{prompt} (e/h): [/bold]")
        return response.lower() in ["e", "evet", "y", "yes"]

    @staticmethod
    def get_text_input(max_len=20):
        """Get text input from user."""
        while True:
            text = console.input(
                f"[bold]Metin girin (max {max_len} kar): [/bold]"
            ).strip()

            if not text:
                console.print("[red]Boş metin![/red]")
                continue

            if len(text) > max_len:
                console.print(f"[red]Çok uzun ({len(text)}/{max_len} kar)![/red]")
                continue

            return text.lower()

    @staticmethod
    def get_name_input():
        """Get name input from user."""
        while True:
            name = console.input("[bold]İsim girin: [/bold]").strip()

            if not name:
                console.print("[red]Boş isim![/red]")
                continue

            if len(name) > 15:
                console.print(f"[red]Çok uzun ({len(name)}/15 kar)![/red]")
                continue

            return name.lower()

    @staticmethod
    def goodbye():
        """Print goodbye message."""
        console.print(
            Panel(
                Text("👋 Güle güle!", style="bold gold1"),
                border_style="cyan",
                padding=(1, 2),
            )
        )
