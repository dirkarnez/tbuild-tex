import subprocess
import time



# https://github.com/dirkarnez/binary-deployer/blob/main/consumer.sh
previous_hash = ""

while True:
    # Pull latest changes quietly
    subprocess.run(["git", "pull", "--quiet"])
    # Get current HEAD hash
    result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True)
    hash = result.stdout.strip()
    print("binary-deployer working...")
    if hash != previous_hash:
        print("hash changed. Deploying")
        # do stuff here
    previous_hash = hash
    time.sleep(1)
