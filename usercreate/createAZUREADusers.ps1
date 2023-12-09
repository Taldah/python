
#Import-Module AzureAD -UseWindowsPowerShell
#Import-Module -SkipEditionCheck -Name AzureAD
#connecting to the Azure AD
connect-AzureAD
# Add-AzureADGroupMember -ObjectId (GroupID) "16bc275b-5846-4bb1-bc32-d9f46a163dc3" -RefObjectId (UserID) "e2f27203-e83f-42d7-a2eb-32a13a96a22d"
$PasswordProfile = New-Object -TypeName Microsoft.Open.AzureAD.Model.PasswordProfile
$PasswordProfile.Password = "Duy45%fs"
#$UPN = 'user1@solargik.com'
#importing the CSV source which has the changes 
$data = Import-Csv '.\createAZUREADusers.csv'
$groups = Import-Csv '.\addgroup.csv'
#Iterating through each row in the CSV
foreach ($row in $data)
{

#INFO in the Console
Write-Host "Creating the user :"  $row.'DisplayName'   $row.'UserPrincipalName'  -ForegroundColor Yellow
#Creating the User
New-AzureADUser -DisplayName $row.'DisplayName' -GivenName $row.'GivenName' -Surname $row.'Surname' -PasswordProfile $PasswordProfile -UserPrincipalName $row.'UserPrincipalName' -JobTitle $row.'JobTitle' -AccountEnabled $true -MailNickName $row.'MailNickName' -Mobile $row.'Mobile' -City $row.'City' -Country $row.'Country' -StreetAddress $row.'StreetAddress'      
#Completion info in the console for the specified row
Write-Host "User has been created" -ForegroundColor Green 

#INFO in the Console
Write-Host "Updating the user :"  $row."User Username"    " manager to "  $row.'Manager Username'  -ForegroundColor Yellow 

#Updating the Manager 
Set-AzureADUserManager -ObjectId (Get-AzureADUser -ObjectId $row.'User Username').Objectid -RefObjectId (Get-AzureADUser -ObjectId $row.'Manager Username').Objectid

#Add user to Group
foreach ($group in $groups) 
{
#INFO in the Consol
Write-Host "add"  $row.'User Username'  "to"  $group.'Sg-Group' -ForegroundColor Yellow

Add-AzureADGroupMember -ObjectId (Get-AzureADGroup -ObjectId $group.'Sg-Group').Objectid -RefObjectId (Get-AzureADUser -ObjectId $row."User Username").Objectid
}
#Completion info in the console for the specified row
Write-Host "Updated." -ForegroundColor Green

}

