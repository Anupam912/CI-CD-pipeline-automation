# powershell/deploy.ps1
param (
    [string]$ImageName = "myapp_image",
    [string]$ServiceName = "myapp_service",
    [string]$DockerfilePath = "..\Dockerfile",
    [string]$AppSourcePath = "..\src",
    [string]$MigrationCommand = "alembic upgrade head"
)

$logFile = "deploy.log"

function Log {
    param([string]$message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "$timestamp $message"
    Write-Host $logEntry
    Add-Content -Path $logFile -Value $logEntry
}

function HealthCheck {
    param([string]$ServiceName)
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:5000/health" -UseBasicParsing
        if ($response.StatusCode -eq 200) {
            Log "Health check for $ServiceName passed."
            return $true
        } else {
            Log "Health check for $ServiceName failed."
            return $false
        }
    } catch {
        Log "Error during health check: $_"
        return $false
    }
}

function Rollback {
    param([string]$ServiceName)
    Log "Rolling back service: $ServiceName"
    docker service rollback $ServiceName
    Log "Rollback completed."
}

# Step 1: Build the Docker image for the new version
Log "Building Docker image for the new version..."
docker build -t $ImageName -f $DockerfilePath $AppSourcePath

# Step 2: Run database migrations (optional)
Log "Running database migrations..."
try {
    Invoke-Expression $MigrationCommand
    Log "Database migrations completed."
} catch {
    Log "Error running migrations: $_"
    exit 1
}

# Step 3: Deploy the new version as a Docker Swarm service
Log "Deploying new version to Docker Swarm..."
try {
    # Create or update the Docker service with rolling update strategy
    docker service update --image $ImageName --update-delay 10s --update-parallelism 1 --update-failure-action rollback $ServiceName
    Log "Service update triggered for: $ServiceName"
} catch {
    Log "Error occurred during service update: $_"
    exit 1
}

# Step 4: Wait for the new service to stabilize
Log "Waiting for service to stabilize..."
Start-Sleep -Seconds 10

# Step 5: Run health check on the new service
if (HealthCheck $ServiceName) {
    Log "New service $ServiceName passed health check."
} else {
    Log "New service $ServiceName failed health check. Initiating rollback."
    Rollback $ServiceName
}
