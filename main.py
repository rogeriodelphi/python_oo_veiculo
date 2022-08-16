import carro

# instanciando o objeto do tipo carro utilizando a classe Carro
# qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado
uno_vermelho = carro.Carro('Vermelho', 4, 'Flex', 1.0, 0, False)
uno_vermelho.ligar()
uno_vermelho.abastecer()
print(f'A quantidade de combustível no Uno Vermelho é: {uno_vermelho.qtd_combustivel}')



uno_preto = carro.Carro('Preto', 4, 'Flex', 1.0, 0, False)
uno_preto.desligar()
print(f'A quantidade de combustível no Uno Preto é: {uno_preto.qtd_combustivel}')