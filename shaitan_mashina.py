def nod(a, b):   # нахождения НОД
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a

def power(a, n):  # возведение в степень
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a, n/2)**2
    else:
        return a*power(a, n-1)

def diffi_helman(p,g,a,b):
	# Public

	if g**(p-1)%p != 1: 
	    raise SystemExit

	# Private
	 # Натуральное число Alice
	# Натуральное число Bob
	# e = 31 # Натуральное число Eve

	# Public
	A = g**a%p # Alice
	B = g**b%p # Bob
	# E = g**e%p # Eve
	print(A, B) # , E

	# Private
	kA = B**a%p # Key
	kB = A**b%p # Key
	# kE = A**e%p # Key
	print(kA, kB) # , kE

import random 

from math import pow

  

a = random.randint(2, 10)

  

def gcd(a, b):

    if a < b:

        return gcd(b, a)

    elif a % b == 0:

        return b;

    else:

        return gcd(b, a % b)

  
# Генерация больших случайных чисел

def gen_key(q):

  

    key = random.randint(pow(10, 20), q)

    while gcd(q, key) != 1:

        key = random.randint(pow(10, 20), q)

  

    return key

  
# Модульное возведение в степень

def power_(a, b, c):

    x = 1

    y = a

  

    while b > 0:

        if b % 2 == 0:

            x = (x * y) % c;

        y = (y * y) % c

        b = int(b / 2)

  

    return x % c

  
# Асимметричное шифрование

def encrypt(msg, q, h, g):

  

    en_msg = []

  

    k = gen_key(q)# Закрытый ключ для отправителя

    s = power_(h, k, q)

    p = power_(g, k, q)

      

    for i in range(0, len(msg)):

        en_msg.append(msg[i])

  

    print("g^k used : ", p)

    print("g^ak used : ", s)

    for i in range(0, len(en_msg)):

        en_msg[i] = s * ord(en_msg[i])

  

    return en_msg, p

  

def decrypt(en_msg, p, key, q):

    dr_msg = []

    h = power_(p, key, q)

    for i in range(0, len(en_msg)):

        dr_msg.append(chr(int(en_msg[i]/h)))

          

    return dr_msg

def ElGamal(msg):


	print("Original Message :", msg)



	q = random.randint(pow(10, 20), pow(10, 50))

	g = random.randint(2, q)



	key = gen_key(q)# Закрытый ключ для получателя

	h = power_(g, key, q)

	print("g used : ", g)

	print("g^a used : ", h)



	en_msg, p = encrypt(msg, q, h, g)

	dr_msg = decrypt(en_msg, p, key, q)

	dmsg = ''.join(dr_msg)

	print("Decrypted Message :", dmsg);

def RSA(m):
	# Вычисление простых чисел #
	array = []
	flag = False
	for s in range(50,125):
		for i in range(2,s):
			if s % i == 0:
				flag = True
				break
		if flag == False:
			array.append(s)
		flag = False
	array.append("...")
	print("s:",array,'\n')

	# Простые числа
	p = 101; q = 53
	print("p = %d; q = %d"%(p,q))

	n = p * q # Произведение
	Fn = (p-1)*(q-1) # Функция Эйлера

	print("n = %d; f(n) = %d\n"%(n, Fn))

	# Подбор открытой экспоненты #
	array = []
	for e in range(1,25):
		d = int((1 + 2 * Fn) / e)
		if d * e == 1 + 2 * Fn:
			array.append(e)
	array.append("...")
	print("e:",array)

	# Открытая экспонента
	e = 3 # Простое нечётное число не имеющее общих делителей с f(n)
	print("e =", e,'\n')

	# Подбор натурального числа k #
	array = []
	for k in range(1,25):
		d = int((1 + k * Fn) / e)
		if d * e == 1 + k * Fn:
			array.append(k)
	array.append("...")
	print("k:",array)

	k = 2 # Натуральное число
	# Секретная экспонента
	d = int((1 + k * Fn) / e)

	print("k = %d; d = %d\n"%(k,d))

	# Условие на вычисление секретной экспоненты
	if d * e != 1 + k * Fn:
		raise SystemExit

	public_key = [e, n] # Публичный ключ
	private_key = [d, n] # Приватный ключ

	print("public_key:",public_key)
	print("private_key:",private_key,'\n')

	#'''
	# Сообщение
	
	print("m =", m)

	# Шифрование
	Cm = m ** e % n
	print("Cm =", Cm)

	# Расшифрование
	Dm = Cm ** d % n
	print("Dm =", Dm)

def main():
	print("""
	[1] Нахождения НОД
	[2] возведение в степень
	[3] Шифр Диффи хэльмана
	[4] Эльгамаль
	[5] RSA
	 """)

	menu = int(input(">"))
	if menu == 0x01:
		a = input("Первое число:")
		b = input("Второе число:")
		print(nod(int(a),int(b)))
	elif menu == 0x02:
		a = input("Первое число:")
		b = input("Второе число:")
		print(power(int(a),int(b)))
	elif menu == 0x03:
		p = input("Простое число:")
		g = input("Натуральное число:")
		a = input("Натуральное число Alice:")
		b = input("Натуральное число Bob:")
		diffi_helman(p,g,a,b)
	elif menu == 0x04:
		msg = input("Сообщение:")
		ElGamal(msg)
	elif menu == 0x05:
		try:
			m = int(input("Число:"))
		except:
			print("Введите число, а не символ!!!!!!")
			exit()
		RSA(int(m))

main()