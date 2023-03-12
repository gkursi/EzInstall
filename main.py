# imports
import os
from colorama import Fore, Back, Style

# title

print(Fore.CYAN+'''
███████╗███████╗██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░
██╔════╝╚════██║██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░
█████╗░░░░███╔═╝██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░
██╔══╝░░██╔══╝░░██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░
███████╗███████╗██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗
╚══════╝╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
'''+Fore.BLUE+"                                                            Generator")
print(Fore.GREEN+"If you need help, refer to the docs at https://github.com/gkursi/EzInstall/blob/main/docs/DOCS.MD ")

# input (for the gen file)
g_name = input(Fore.WHITE+'Enter your desired file name (without file extension): ')
g_dir = r"output\\"

# input (for the installation)

o_filehost = ''
o_pack_count = ''
o_packs = []
o_instal_dir = ''

try: 
    o_filehost = input("Enter the source zip file host URL (you can use github): ")
    o_pack_count = input("Enter how many dependencies you want to install (0 for none): ")
    o_packs = []
    for i in range(int(o_pack_count)):
        o_packs.append(input(f"[{i}] Enter the dependencie url: "))
    o_instal_dir = input(r"Enter the directory you want your app to be installed in (things like %appdata% can be used): ")
except Exception as err:
    print(f'Exception while parsing input (2): \n'+str(err))
# magic

o_dep_str = ''''''
for i in range(int(o_pack_count)):
    o_dep_str+='''

    curl '''+o_packs[i]+''' -o dependencie.zip >nul
    tar -xf dependencie.zip
    del dependencie.zip

    '''

output_script_batch = '''
@ECHO off
echo [-------------------------------------------------------------------]
echo 	Installer script
echo                                                               V 0.01
echo [-------------------------------------------------------------------]

@REM binary installation
echo Preparing for binary installation...
mkdir '''+o_instal_dir+'''
cd '''+o_instal_dir+'''
echo Downloading files...
curl '''+o_filehost+''' -o archive.zip >nul
echo Installing... 
tar -xf archive.zip
echo Cleaning up...
del archive.zip

@REM dependecie installation
echo Preparing for dependencie installation...
mkdir dependencies
cd dependencies
echo Installing dependencies...
'''+o_dep_str+'''

echo Done!
echo Press any key to exit installation..

'''

g_path = g_dir+g_name+'.bat'

os.system('mkdir '+g_dir)
os.system('cd '+g_dir)
os.system('echo @ECHO off >'+g_path)
f = open(g_path, 'w')
f.write(output_script_batch)
f.close()
print(Fore.GREEN+'Resulted script located at '+g_path)
print(Fore.WHITE+'Press any key to exit...')
os.system('pause >nul')

