# Script para adicionar uma nova regra de execução de aplicativo no Editor de Política de Grupo Local

# Caminho do executável a ser permitido
$caminhoExecutavel = "C:\Caminho\Para\Seu\Arquivo.exe"

# Instanciando o objeto do Editor de Política de Grupo Local
$editorPolitica = New-Object -ComObject "MMC20.Application"
$editorPolitica.Load("gpedit.msc")

# Navegando até as Regras de Execução de Aplicativo
$grupoPoliticadeSeguranca = $editorPolitica.Document.ActiveView.ScopeNode.GetNode(1).Children | Where-Object {$_.DisplayName -eq "Políticas de Segurança"}
$controleExecucaoAplicativo = $grupoPoliticadeSeguranca.Children | Where-Object {$_.DisplayName -eq "Controle de Execução de Aplicativo"}

# Criando uma nova regra de caminho
$novaRegra = $controleExecucaoAplicativo.Children.Add("1", "Regra de Caminho")

# Configurando a nova regra
$novaRegra.PolicyItem.DataItem.Name = $caminhoExecutavel
$novaRegra.PolicyItem.DataItem.SecurityLevel = 2 # Permitir a execução deste arquivo

# Salvando as alterações
$editorPolitica.FileSaveAll()
