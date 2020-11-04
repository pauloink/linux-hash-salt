import crypt, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) <= 1:
    print(f"{bcolors.HEADER}=============================================================================================={bcolors.ENDC}")
    print("")
    print(f"{bcolors.OKBLUE}\tScript para quebra de senha em hash + salt no arquivo shadow do linux.{bcolors.ENDC}")
    print("")
    print(f"{bcolors.OKBLUE}\t[+] Modo de utilizacao: {bcolors.ENDC}"+f"{bcolors.UNDERLINE}python3 Ink_Hash_Salt.py 'wordlist_de_sua_preferencia' {bcolors.ENDC}")
    print("")
    print(f"{bcolors.HEADER}=============================================================================================={bcolors.ENDC}")
    print("")


else:
    print(f"{bcolors.HEADER}=============================================================================================={bcolors.ENDC}")
    print("")

    wordlist = open(sys.argv[1]).read().splitlines()

    _hash = input(f"{bcolors.OKBLUE}\tDigite o hash completo, incluindo o salt: {bcolors.ENDC}")
    print("")
    _salt = input(f"{bcolors.OKBLUE}\tDigite o salt: {bcolors.ENDC}")

    print(f"{bcolors.HEADER}=============================================================================================={bcolors.ENDC}")
    print("")

    for bruteforce in wordlist:
        gen_hash = crypt.crypt(bruteforce, _salt)
        if gen_hash == _hash:
            print(f"{bcolors.OKGREEN}\tSenha encontrada: {bcolors.ENDC}"+bruteforce)
            break
        else:
            print(f"{bcolors.FAIL}\tFalhou: {bcolors.ENDC}"+bruteforce)
            continue

    print(f"{bcolors.HEADER}=============================================================================================={bcolors.ENDC}")
