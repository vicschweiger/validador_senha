def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  for char in senha:
    if char.isupper():
      tem_letra_maiuscula = True
    elif char.islower():
      tem_letra_minuscula = True
    elif char.isdigit():
      tem_numero = True
    elif not char.isalnum():
      tem_caractere_especial = True


  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  if tem_letra_minuscula and tem_numero and tem_caractere_especial:
    return "Sua senha atende aos requisitos de seguranca. Parabens!"
  else:
    return "Sua senha nao atende aos requisitos de seguranca."

senha = input().strip()

resultado = verificar_forca_senha(senha)

print(resultado)