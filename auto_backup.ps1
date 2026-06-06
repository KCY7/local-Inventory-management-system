# ==========================================
# HCC INVENTORY - AUTOMATED SQLITE BACKUP
# ==========================================

# 1. PATH TO YOUR DEPLOYED DATABASE (UPDATE THIS!)
$sourceDB = "C:\PATH_TO_YOUR_APP\HCC_Inventory\db.sqlite3"

# 2. DYNAMIC GOOGLE DRIVE SEARCH
# We search all available drives (C:\, D:\, G:\, H:\, etc.) for the backup folder
$targetSubFolder = "My Drive\HCC_Database_Backups"
$driveFolder = $null

foreach ($drive in (Get-PSDrive -PSProvider FileSystem).Root) {
    $testPath = Join-Path $drive $targetSubFolder
    if (Test-Path $testPath) {
        $driveFolder = $testPath
        break
    }
}

# If the drive isn't found, stop the script safely
if (-not $driveFolder) {
    Write-Warning "Backup failed: Google Drive folder not found."
    exit
}

# ==========================================
# DO NOT CHANGE ANYTHING BELOW THIS LINE
# ==========================================

# The New Standard: Adds Year-Month-Day AND Hour-Minute-Second
$date = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$destination = "$driveFolder\db_backup_$date.sqlite3"

# Copy the database file to Google Drive silently
Copy-Item -Path $sourceDB -Destination $destination -Force

# Retention Policy: Keep only the last 30 days of backups to save Drive space
$daysToKeep = 30
$limitDate = (Get-Date).AddDays(-$daysToKeep)

# Sweeps the old files into the trash
Get-ChildItem -Path $driveFolder -Filter "db_backup_*.sqlite3" | 
    Where-Object { $_.LastWriteTime -lt $limitDate } | 
    Remove-Item -Force