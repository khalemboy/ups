# Create Banner IG And FB

try:
    import re, os, sys, time
    from rich.panel import Panel
    from rich.console import Console
    from Temporary.Terminalize.Styles import style_terminal
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6285767630210?text=BANNER%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6285767630210?text=BANNER%20ERROR%20%3A%20{quote(str(e))}')
        exit()

class Terminal:
    def __init__(self) -> None:
        self.Layar_Terminal()
        pass
        
    def clear_terminalize(self):
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        
    def Banner_Facebook(self):
        self.clear_terminalize()
        Console(width = 65, style = f"{style_terminal}").print(Panel("""[red] ●[yellow] ●[green] ●[red]  
 ____  _  _  ___  ____   __       ____  ____   ___ 
(_  _)( \( )/ __)(_  _) /__\  ___( ___)(  _ \ / __)
 _)(_  )  ( \__ \  )(  /(__)\(___))__)  ) _ <( (__ 
(____)(_)\_)(___/ (__)(__)(__)   (__)  (____/ \___)
[red] ●[yellow] ●[green] ●[red]  
    """, title = "[white]• [green]ArifXeyracode[white] •"))
        return (True)
        
    def Banner_Instagram(self):
        self.clear_terminalize()
        Console(width = 65, style = f"{style_terminal}").print(Panel("""[red] ●[yellow] ●[green] ●[red]          
 ____  _  _  ___  ____   __       ____  ____   ___ 
(_  _)( \( )/ __)(_  _) /__\  ___( ___)(  _ \ / __)
 _)(_  )  ( \__ \  )(  /(__)\(___))__)  ) _ <( (__ 
(____)(_)\_)(___/ (__)(__)(__)   (__)  (____/ \___)
[red] ●[yellow] ●[green] ●[red]  
    """, title = "[white]• [green]ArifXeyracode[white] •"))
        return (True)
       
    def Layar_Terminal(self):
        self.get_terminal_size = re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)
        if int(self.get_terminal_size) < 65:
            Console(width = 65, style = f"{style_terminal}").print(Panel("[italic grey50]Anda Diwajibkan Untuk Mengecilkan Tampilan Termux Sampai Kotak Ini Terlihat Rapi!", title=f"[white]• [red]Eror Not Found [white]•"))
            exit()
        else:
            pass
            
