
# Cookie Dough Exstention
# Login Cookie Facebook

try:
    import requests, re, time, os
    from rich.panel import Panel
    from rich.console import Console
    from Penyimpanan.Banner import Terminal
    from Temporary.Terminalize.Styles import style_terminal
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6285767630210?text=TokenEAAB%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6285767630210?text=TokenEAAB%20ERROR%20%3A%20{quote(str(e))}')
        exit()

class Token:
    def __init__(self) -> None:
        self.data = '/sdcard/data/login/'
        pass
        
    def TokenEAAB(self, cookies, url = 'https://www.facebook.com/adsmanager/manage/campaigns'):
        with requests.Session() as r:
            try:
                response = r.get(url, cookies = {'cookie': cookies}).text
                try:
                    self.act = re.search('act=(.*?)&nav_source',str(response)).group(1)
                except (Exception) as e:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[italic grey50]{str(e).title()}", title = f"[white]• [red]Cookies Invalid [white]•"))
                    exit()
                response2 = r.get(url+f'?act={self.act}&nav_source=no_referrer&breakdown_regrouping=1', cookies = {'cookie': cookies}).text
                return (re.search('accessToken="(.*?)"',str(response2)).group(1))
            except (AttributeError, requests.exceptions.ConnectionError) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[italic grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()                