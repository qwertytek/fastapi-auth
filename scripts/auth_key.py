import subprocess

result = subprocess.run(["openssl", "rand", "-hex", "32"], capture_output=True, text=True)

secret_key = result.stdout.strip()

with open(".env", "a") as env_file:
    env_file.write(f"AUTH_SECRET_KEY={secret_key}\n")

