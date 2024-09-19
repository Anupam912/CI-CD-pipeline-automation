# powershell/build.ps1
param (
    [string]$ProjectPath = "..\src"
)

$logFile = "build.log"

function Log {
    param([string]$message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "$timestamp $message"
    Write-Host $logEntry
    Add-Content -Path $logFile -Value $logEntry
}

Log "Starting build process for project in $ProjectPath"

try {
    Start-Process -FilePath "python" -ArgumentList "$ProjectPath\app.py"
    Log "Build completed successfully."
} catch {
    Log "Error occurred during build: $_"
    exit 1
}
