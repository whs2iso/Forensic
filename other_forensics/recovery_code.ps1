$count_drive_letter = "E:"

$recovery_key1 = "574783-056749-579095-431145-710270-240900-"
$recovery_key7 = ""
$recovery_key8 = "-560197"

for ($count = 0; $count -le 1000000; $count++){
    $recovery_key7 = $count.ToString()
    
    if ($recovery_key7.Length -lt 6){
        $padd = "0" * (6 - $recovery_key7.Length)
        $recovery_key7 = $padd + $recovery_key7
    }

    $beauty_recovery_key = $recovery_key1 + $recovery_key7 + $recovery_key8
    $recovery_key = $beauty_recovery_key.replace("-", "")

    try{
        Unlock-BitLocker -MountPoint $count_drive_letter -RecoveryPassword $recovery_key -ErrorAction Stop
        Write-Output "[$count] Matched!! : $beauty_recovery_key"
        break
    }
    catch [System.Runtime.InteropServices.COMException]{
        Write-Output "[$count] Failed Recovery Key: $beauty_recovery_key"
    }
}