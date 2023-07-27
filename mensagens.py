from sty import fg

menu = """
    
    [1]. Criar Usuario
    [2]. Criar Conta Corrente
    [3]. Listar Usuarios
    [4]. Listar Conta Corrente
    [5]. Depositar
    [6]. Sacar
    [7]. Extrato
    [8]. Sair
    
=>"""

final = fg.li_blue + "Obrigado! por utlizar nosso sistema" + fg.rs

formato_endereco = "logradouro-numero-bairro-cidade/UF"

erro = "[ERRO]:"
erro_opcao = fg.red + f"{erro} Opção Não Encontrada, Por favor digite os números do menu" + fg.rs
erro_valor_negativo = fg.red + f"{erro} Valor Negativo" + fg.rs
erro_limite_saque = fg.red + f"{erro} Limite Diario de Saque Ultrapassado" + fg.rs
erro_limite_saldo = fg.red + f"{erro} Valor Do Saldo Ultrapassado" + fg.rs
erro_limite_valor_saque = fg.red + f"{erro} Valor Limite De Saque Da Sua Conta Utrapassado" + fg.rs

erro_cpf_existente = fg.red + f"{erro} Esse CPF já existe no Sistema" + fg.rs
erro_usuario_nao_encontrado = fg.red + f"{erro} Usuario Não Encontrado" + fg.rs
erro_usuario_nao_tem_conta = fg.red + f"{erro} Usuario Informado Não Possui C/c" + fg.rs
erro_usuario_cadastro = fg.red + f"{erro} Houve Um Erro No Cadastro desse Usuario, por favor tente novamente" + fg.rs

sucesso = "[SUCESSO]"
sucesso_saque = fg.green + f"{sucesso} Operação Saque Realizada Com Sucesso" + fg.rs
sucesso_criacao_cc = fg.green + f"{sucesso} Operação de Criar Conta Corrente Realizada Com Sucesso" + fg.rs
sucesso_criacao_cliente = fg.green + f"{sucesso} Operação de Cadastro de Cliente Realizada Com Sucesso" + fg.rs
sucesso_deposito = fg.green + f"{sucesso} Operação Deposito Realizada Com Sucesso" + fg.rs
