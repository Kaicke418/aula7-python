ecommerce ={
   'tablet':500,
   'livro':250,
   'fone':1500,
   'formas_pag':['pix','cc', 'cd', 'boleto']
}


print(ecommerce['formas_pag'][0])


escolha1 = input('Digite o nome do produto ') 
print('produto escolhido', ecommerce[escolha1])

escolha2 = input('escolha outro produto ')
print('produto escolhido', ecommerce[escolha2])

escolha3 = input('escolha outro produto ')
print('produto escolhido', ecommerce[escolha3])

forma_de_pag = int(input('qual sua forma de pagamento? '))
print(f'ok, forma de pagamento: {ecommerce["formas_pag"][forma_de_pag]}')
print('pagamento realizado')

# ecommerce = {
#    'fones':200,
#   'computadores':500
 
# }


# valores = []
# carrinho = []


# escolha1 = input('Digite seu produto')
# escolha2 = input('Digite seu produto')


# carrinho.append(escolha1)
# carrinho.append(escolha2)


# valores.append(ecommerce[escolha1])
# valores.append(ecommerce[escolha2])


# soma = sum(valores)


# print('Total', soma)








# # 1 comprar
# # carrinho = []
# # valores  =  []
# # escolha_produto1 = input('escolha produto _ fones, computadores')
# # tipo_produto1 = int(input('Escolha tipo x, n, r '))
# # escolha_produto2 = input('escolha produto _ fones, computadores')
# # tipo_produto2 = int(input('Escolha tipo x, n, r '))




# # carrinho += (ecommerce[escolha_produto1][tipo_produto1], ecommerce[escolha_produto2][tipo_produto2])

