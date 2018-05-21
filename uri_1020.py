idade = int(input())

ano = int(idade / 365)
mes = int((idade%365/30))
dias = int(idade%365%30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(ano,mes,dias))