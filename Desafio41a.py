# Categoriza um atleta conforme ano de nascimento.
from datetime import date
print('\033[34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[34m-+-\033[m' * 20)
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('A idade é de {} anos.'.format(idade))
if idade <= 9:
    print('O atleta pertence à categoria \033[34mMIRIM\033[m.')
elif idade <= 14:
    print('O atleta pertence à categoria \033[34mINFANTIL\033[m.')
elif idade <= 19:
    print('O atleta pertence à categoria \033[34mJUNIOR\033[m.')
elif idade <= 25:
    print('O atleta pertence à categoria \033[34mSÊNIOR\033[m.')
else:
    print('O atleta pertence à categoria \033[34mMASTER\033[m.')
