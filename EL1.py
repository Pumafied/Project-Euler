PC = 1
add = 0
while PC < 1000:
	if PC%5 == 0:
		add = add + PC;
	elif PC%3 == 0:
		add = add + PC;		
	PC += 1;
print PC;	
print add;
