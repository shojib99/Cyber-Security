import subprocess


def get_browser_connections():
    # Common Windows browser process names
    browsers = [
        'chrome.exe',
        'firefox.exe',
        'msedge.exe',
        'brave.exe',
        'opera.exe',
    ]

    print('Gathering active browser connections...\n')
    print(f"{'Browser':<15} | {'Local Port':<12} | {'Remote IP':<18}")
    print('-' * 50)

    try:
        # 1. Ask Windows for a list of all running processes to match Process IDs (PIDs) to names
        tasklist = subprocess.check_output('tasklist', shell=True, text=True)
        pid_to_name = {}

        for line in tasklist.splitlines():
            parts = line.split()
            # If the line looks like process info (has a name and a PID number)
            if len(parts) > 1 and parts[1].isdigit():
                pid_to_name[parts[1]] = parts[0].lower()

        # 2. Ask Windows for all active network connections
        netstat = subprocess.check_output('netstat -ano', shell=True, text=True)

        found = False
        for line in netstat.splitlines():
            # We only care about active (ESTABLISHED) connections
            if 'ESTABLISHED' in line:
                parts = line.split()
                if len(parts) >= 5:
                    local_ip_port = parts[1]
                    remote_ip_port = parts[2]
                    pid = parts[-1]

                    # Look up the name using the PID
                    name = pid_to_name.get(pid, 'unknown')

                    if name in browsers:
                        # Extract just the port and the IP
                        local_port = local_ip_port.split(':')[-1]
                        remote_ip = remote_ip_port.rsplit(':', 1)[0]

                        print(
                            f'{name:<15} | {local_port:<12} | {remote_ip:<18}'
                        )
                        found = True

        if not found:
            print(
                'No active browser connections found. (Try loading a website first).'
            )

    except Exception as e:
        print(f'An error occurred: {e}')


# Corrected double underscores for __name__ and __main__
if __name__ == '__main__':
    get_browser_connections()

    # This stops the window from closing instantly when you double-click it
    input('\nPress Enter to exit...')