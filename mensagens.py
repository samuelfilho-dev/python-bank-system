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
erro_limite_valor_saque = fg.red + f"{erro} Valor Limite é R$ 500,00" + fg.rs

erro_cpf_existente = fg.red + f"{erro} Esse CPF já existe no Sistema" + fg.rs
erro_usuario_nao_encontrado = fg.red + f"{erro} Usuario Não Encontrado" + fg.rs
erro_usuario_cadastro = fg.red + f"{erro} Houve Um Erro No Cadastro desse Usuario, por favor tente novamente" + fg.rs
