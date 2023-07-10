from sty import fg

menu = """

    [1]. Depositar
    [2]. Sacar
    [3]. Extrato
    [4]. Sair
    
=>"""

final = "Obrigado! por utlizar nosso sistema"

erro = "[ERRO]:"
erro_opcao = fg.red + f"{erro} Opção Não Encontrada, Por favor digite os números do menu" + fg.rs
erro_valor_negativo = fg.red + f"{erro} Valor Negativo" + fg.rs
erro_limite_saque = fg.red + f"{erro} Limite Diario de Saque Ultrapassado" + fg.rs
erro_limite_saldo = fg.red + f"{erro} Valor Do Saldo Ultrapassado" + fg.rs
erro_limite_valor_saque = fg.red + f"{erro} Valor Limite é R$ 500,00" + fg.rs
