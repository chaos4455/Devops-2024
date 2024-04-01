# Função para testar o login RDP
function Testar-RDPLogin {
    param (
        [string]$ip,
        [int]$porta,
        [System.Management.Automation.PSCredential]$credenciais
    )

    # Tentando estabelecer uma sessão remota
    $session = New-PSSession -ComputerName $ip -Port $porta -Credential $credenciais -ErrorAction SilentlyContinue

    # Verificando se a sessão foi estabelecida com sucesso
    if ($session) {
        # Encerrando a sessão
        Remove-PSSession -Session $session
        return $true
    } else {
        return $false
    }
}

# Solicitar credenciais ao usuário
$credenciais = Get-Credential -Message "Por favor, insira suas credenciais de login para RDP" -UserName "localhost\Administrador"

# Lista de hosts e portas
$hosts = @(
    @{ IP = "gruponaka.ddns.com.br"; Porta = 3503 }
    # Adicione mais hosts conforme necessário
)

# Iterar sobre cada host
foreach ($hostInfo in $hosts) {
    $ip = $hostInfo.IP
    $porta = $hostInfo.Porta

    # Testar o login RDP
    $loginValido = Testar-RDPLogin -ip $ip -porta $porta -credenciais $credenciais

    # Exibir resultado
    if ($loginValido) {
        Write-Host "Login válido para $ip na porta $porta." -ForegroundColor Green
    } else {
        Write-Host "Login inválido para $ip na porta $porta. Verifique as credenciais fornecidas." -ForegroundColor Red
    }
}
