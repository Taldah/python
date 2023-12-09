$Foldername = "C:\Program Files (x86)\Teleport"
$Reponame = "C:\Repos\support-projects"
$tshpath = "C:\Users\$env:username\AppData\Local\Programs\teleport-connect\resources\bin\tsh.exe"
$tshdes = "C:\Program Files (x86)\Teleport\tsh.exe"
$pathContent = [Environment]::GetEnvironmentVariable('path')
$myPath = "C:\Program Files (x86)\Teleport"
if (Test-Path $Foldername) {
    Write-Host "Folder Exists"
}
else {
    New-Item $Foldername -ItemType Directory
    Write-Host "Folder created successfully & file was copyed!"
}
if (Test-Path $Reponame) {
  Write-Host "Folder Exists"
}
else {
  New-Item $Reponame -ItemType Directory
  Write-Host "Folder created successfully"
}
if (Test-Path $tshdes) {
  Write-Host "tsh file Exists"
}
else {
  Copy-Item -Path $tshpath  -Destination $Foldername
  Write-Host "file was copyed!"
}

if ($pathContent -ne $null)
{
  # "Exist in the system!"
  if ($pathContent -split ';'  -contains  $myPath)
  {
    # My path Exists
    Write-Host "$myPath exists" -ForegroundColor Green
  }
  else
  {
    #Set-Item -Path Env:\Path -Value "C:\Program Files (x86)\Teleport"
    setx PATH "$env:path;C:\Program Files (x86)\Teleport" -m
    Write-Host "$myPath does not exist"
  }
}
