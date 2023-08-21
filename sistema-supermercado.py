from time import sleep
print('=' * 20)
print('Supermercado Compre Tudo')
print('=' * 20)
sleep(1)
total = 0
while True:
    produto = str(input('Qual o nome do produto? ')).title()
    sleep(1)
    preço = float(input('Qual o preço desse produto? R$'))
    sleep(1)
    total += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja adicionar mais produtos? ')).strip().upper()[0]
    if resp == 'N':
        break

sleep(1.5)
print('Agora selecione a sua forma de pagamento')
print('''[1]Para pagar no dinheiro com 10% de desconto;
[2]Para pagar no pix também com 10% de desconto;
[3]à vista no cartão com cartão com 5% de desconto;
[4]até 2x no cartão ou
[5]3x ou mais no cartão com 20% de juros no valor total.''')
formPag = 0
while formPag not in (1, 2, 3, 4, 5):
    formPag = int(input('Qual a opção de pagamento? '))
if formPag == 1:
    if total > 200:
        totalPag = total - (total * 10 / 100)
        print(f'Para compras acima de R$200, aplicamos o desconto de 10%, o total a ser pago será de R${totalPag:.2f}')
        valorRec = float(input('Dinheiro recebido: R$'))
        troco = valorRec - totalPag
        print(f'Troco: R${troco:.2f}')
    else:
        print(f'Valor total da compra R${total}')
        valorRec = float(input('Dinheiro recebido: R$'))
        troco = valorRec - total
        sleep(2)
        print(f'Troco: R${troco:.2f}')
elif formPag == 2:
    if total >= 100:
        totalPag = total - (total * 10 / 100)
        print(f'Para compras acima de R$100 aplicamos o cupom de 10% de desconto, total fica por R${totalPag}')
    else:
        print(f'Valor total da compra R${total}')
elif formPag == 3:
    totalPag = total - (total * 5 / 100)
    print(f'Para pagamentos à vista no cartão oferecemos 5% de desconto, o total fica por R${totalPag}')
elif formPag == 4:
    print(f'Para pagamentos em até 2x no cartão paga o valor normal, total fica por R${total}')
elif formPag == 5:
    totalPag = total + (total * 20 / 100)
    print(f'Para pagamentos em 3x ou mais no cartão tem um acréscimo de 20% de juros, total fica por R${totalPag}')
print('Agradecemos a preferência.')
print('Volte sempre!')




