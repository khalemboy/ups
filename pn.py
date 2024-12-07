from Penyimpanan.FolderSC.instagram import Instagram
from rich.panel import Panel
from rich.console import Console
from Temporary.Terminalize.Styles import style_terminal
M2 = '[bold red]' # MERAH
H2  = '[bold green]' # HIJAU

KG = '\x1b[1;93m' # KUNING
BU = '\x1b[1;94m' # BIRU

UU = '\x1b[1;95m' # UNGU
P2 = '[bold white]' # DEFAULT

try:
    import os, re, sys, json, time, datetime, requests
    from rich.panel import Panel
    from rich.console import Console
    from Penyimpanan.FolderSC.instagram import Instagram
    from Penyimpanan.Banner import Terminal
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6285767630210?text=LICENSE%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6285767630210?text=LICENSE%20ERROR%20%3A%20{quote(str(e))}')
        exit()

class LicenseKey:
    def __init__(self) -> None:
        self.dire = 'data/user/login'
        self.byps = Instagram()
        self.data,self.user,self.login = ('data'), ('user'), ('login')
        self.CreateDir()
        self.CekKeys()

    def CreateDir(self):
        try:os.mkdir(self.data)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user +'/'+ self.login)
        except:pass

    def Keys(self):
        Terminal().clear_terminalize()
        Console().print(f'\n {P2}[{H2}+{P2}] Belum memiliki license? ketik ({H2}beli{P2}) untuk membeli license key!')
        auth = Console().input(f' {P2}[{H2}?{P2}] Masukan License : ')
        xnxx = auth.lower()
        if auth == 'beli' or xnxx == 'beli' or auth == 'beli':
           Console().print(f'\n [{H2}Premium Instagram And Facebook{P2}]\n\n {H2}01{P2}. 1 Minggu   : {H2}200.000\n {H2}02{P2}. 2 Minggu   : {H2}300.000\n {H2}03{P2}. 3 Minggu   : {H2}400.000\n {H2}04{P2}. 1 Bulan    : {H2}500.000\n\n {H2}L{P2}.Open source Script Lama :{H2}1.50.000\n {H2}T{P2}.Permanen Open source Terbaru{H2}2.50.000')
           choose = Console().input(f'\n {P2}[{H2}?{P2}] Choose : ')
           if choose =='1' or choose =='01':
              os.system(f'xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20license%20yang%201%20minggu%20dong') ; time.sleep(2) ; self.Keys()
           elif choose =='2' or choose =='02':
               os.system(f'xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20license%20yang%202%20minggu%20dong') ; time.sleep(2) ; self.Keys()
           elif choose =='3' or choose =='03':
               os.system(f'xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20license%20yang%203%20minggu%20dong') ; time.sleep(2) ; self.Keys()
           elif choose =='4' or choose =='04':
               os.system(f'xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20license%20yang%201%20bulan%20dong') ; time.sleep(2) ; self.Keys()
           elif choose =='L' or choose =='p':
               os.system(f'xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20license%20yang%20Permanen%20dong') ; time.sleep(2) ; self.Keys()
           elif choose =='T' or choose =='o':
               os.system(f'xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20Open%20Sourcenya%20dong') ; time.sleep(2) ; self.Keys()
        else:
           if len(auth) <=5:exit()
           else:self.confirm(auth)

    def confirm(self, keys, token = 'WyIxMDAyMDQwMDkiLCJXVFEwdnpRMG5iZ2RzZEVPM1ZKTkgyWDVZNzZhRHlxNHNqVEtnbHJDIl0=', produc_id='28333'):
        skrg = datetime.datetime.now()
        hari = skrg.day
        buln = skrg.month
        thun = skrg.year
        try:
            link = requests.get("https://app.cryptolens.io/api/key/Activate?token={}&ProductId={}&Key={}".format(token,produc_id,keys)).json()
            crtd = link["licenseKey"]["created"][:10]
            expd = link["licenseKey"]["expires"][:10]
            tahun,bulan,tanggal = expd.split("-")
            date = "%s%s%s"%(int(tanggal),int(bulan),int(tahun))
            form = "%d%m%Y"
            neww = "%s%s%s"%(hari,buln,thun)
            tess = datetime.datetime.strptime(date,form)
            mekk = datetime.datetime.strptime(neww,form)
            xdxx = tess - mekk
            sisa = xdxx.days
            if sisa <1:
               os.system(f'rm -rf {self.dire}/key.txt')
               Console().print(f'\n {P2}[{M2}!{P2}] {M2}LicenseKey{P2} anda sudah kedaluarsa!'); self.Keys()
            else:
               Terminal().clear_terminalize()
               open(self.dire+'/key.txt','w',encoding='utf-8').write(f'{keys}')
               open(self.dire+'/day.txt','w',encoding='utf-8').write(f'{sisa}')
               self.byps.Chek_Cookies(crtd,expd,sisa)
        except KeyError:
           os.system(f'rm -rf {self.dire}/key.txt')
           Console().print(f'\n {P2}[{M2}!{P2}] {M2}LicenseKey{P2} anda invalid!!'); self.Keys()
        except Exception as e: print(e)

    def CekKeys(self):
        if os.path.isfile(f'{self.dire}/key.txt') is True:
           keys = open(self.dire+'/key.txt','r').read()
           self.confirm(keys)
        else:
           self.Keys()
LicenseKey()       
        
