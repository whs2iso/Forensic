import subprocess

# 변수 설정
count_drive_letter = "E:"

recovery_key1 = "574783-056749-579095-431145-710270-240900-"
recovery_key8 = "-560197"

# 루프 설정
for count in range(1000001):
    recovery_key7 = str(count).zfill(6)

    beauty_recovery_key = recovery_key1 + recovery_key7 + recovery_key8
    recovery_key = beauty_recovery_key.replace("-", "")

    try:
        # BitLocker 해제 시도
        command = f'Unlock-BitLocker -MountPoint {count_drive_letter} -RecoveryPassword "{recovery_key}"'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, check=True)

        print(f"[{count}] Matched!! : {beauty_recovery_key}")
        break
    except subprocess.CalledProcessError as e:
        print(f"[{count}] Failed Recovery Key: {beauty_recovery_key}")
        print(f"Error: {e.stderr}")

    except Exception as ex:
        print(f"Unexpected error: {ex}")
