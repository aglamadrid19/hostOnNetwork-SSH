### Find available hosts in our network and list the ones with port 22 (SSH) open.

# Initialize Array to contain on-hosts (ping) and listening on port 22 (SSH)
$onNetHosts = @();
$openSSH = @();

# Get Computer IP address.
$currentIPAddress = Read-Host -Prompt "Input your IP Address";
$strippedLastOctet = $currentIPAddress.Substring(0, $currentIPAddress.LastIndexOf('.'));

# For loop to ping /24 addresses (1 time only)
For ($i = 1; $i -le 255; $i++) {
    $createdIP = "$strippedLastOctet." + [string]$i;
    if (Test-Connection -IPv4 -Count 1 $createdIP -Quiet) {
        $onNetHosts += $createdIP;
        # Check for SSH or port 22 open
        if (Test-Connection -TCPPort 22 -ComputerName $createdIP -Quiet) {
            $openSSH += $createdIP;
        }
    }
}

# List Of Hosts
Write-Output "***Host Currently on the Network***";
Write-Output $onNetHosts;
Write-Output "***Host Currently on the Network and Port 22 (SSH) listening***";
Write-Output $openSSH;