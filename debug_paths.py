import subprocess

def run_command(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True).decode().strip()
        return out
    except Exception as e:
        return f"Erro executando '{cmd}': {e}"

def main():
    cmds = [
        "which chromium",
        "which chromium-browser",
        "which chromedriver",
        "ls -l /usr/bin/chromedriver",
        "ls -l /usr/bin/chromium",
        "ls -l /usr/bin/chromium-browser"
    ]
    for c in cmds:
        result = run_command(c)
        print(f">>> {c} => {result}")

if __name__ == "__main__":
    main()
