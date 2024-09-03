while True:
#aqui colocamos uma mensagem para o cliente.
  print ("BEM VINDO A CALCULADORA DE IMC")
#aqui solicitamos as entradas do peso e da altura do cliente.
  altura=float(input("Digite a sua altura (em m)"))
  peso=float(input("Digite seu peso (em kg)"))
#aqui realizamos o calculo do IMC, de acordo, como deve ser feito.
  IMC=peso/(altura*altura)
#aqui classificamos o IMC de acordo com o seu numero e exibimos a situacao do IMC do usuario
  if IMC<18.5:
    print ("Seu IMC e",IMC,"esta classificado como abaixo do peso")
  if 18.5<IMC<24.9:
    print ("Seu IMC e",IMC,"esta classificado como ideal")
  if 24.9<IMC<29.9:
    print ("Seu IMC e",IMC,"esta classificado como sobrepeso")
  if 30<IMC<34.9:
    print ("Seu IMC e",IMC,"esta classificado como obesidade grau I")
  if 35<IMC<39.9:
    print("Seu IMC e",IMC,"esta classificado como obesidade grau II")
  if IMC>40:
    print ("Seu IMC e",IMC,"esta classificado como obesidade morbida")
#aqui perguntamos ao usuario se ele gostaria de repetir a operacao
  repetir=(input('Voce deseja calcular o imc novamente?(Digite s para sim e n para nao)'))
  if repetir!="s":
    break
#mensagem de despedida.
print ("Obrigado por utilizar essa calculadora de IMC")