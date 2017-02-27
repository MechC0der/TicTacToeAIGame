import random
import os
os.system('cls')

#ask for letter
def ask():
	logo = ' '
	
	while not (logo=='X' or logo=='O'):
		print('Choose your letter [Either X or O]')
		logo = input().upper()
		
	if logo=='X': return ['X','O']
	else: return ['O','X']
	
#decide who plays first
def coin():
	if random.randint(0,1):
		return 'Player'
	else:
		return 'AI'

#show the updated game
def show(b):
	print('		',b[7],"|",b[8],"|",b[9])
	print("		----------")
	print('		',b[4],"|",b[5],"|",b[6],'		TTT AI by PP \\m/')
	print("		----------")
	print('		',b[1],"|",b[2],"|",b[3])
	
#check if space is available
def available(mat,num):
	return mat[num] == ' '
	
#take player's move
def playerMove(b):
	num = '0'
	
	while int(num)<1 or int(num)>9 or not available(mat,int(num)):
		print('Your turn')
		num = input()
		
	return int(num)
	
#Make the move in the game
def makeMove(b,mov,logo):
	b[mov] = logo
	
#copy the mat
def copyMat(a):
	copied = []
	
	for i in a:
		copied.append(i)
		
	return copied
	
#Random place checker
def randomPlace(b,lis):
	pos = []
	for i in lis:
		if available(b,i):
			pos.append(i)
			
	if len(pos):
		return random.choice(pos)
	else:
		return None
		
#take AI move
def aiMove(mat,ai):
	if ai=='X': pl='O'
	else: pl='X'
	
	for i in range(1,10): #Check if AI can win
		b = copyMat(mat)
		if available(b,i):
			makeMove(b,i,ai)
			if win(b,ai):			
				return i
	
	for i in range(1,10): #Check if AI can lose
		b = copyMat(mat)	
		if available(b,i):
			makeMove(b,i,pl)
			if win(b,pl):
				return i
				
	if available(mat,5): #check center
		return 5
						
	move = randomPlace(mat,[1,3,7,9]) #Check if corners are free
	if move != None:
		return move
			
	return randomPlace(mat,[2, 6, 4,8]) #Give away the spaces

#ask to play again
def again():
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')

#winning game condition
def win(b,l):
	return ((b[1]==b[2]==b[3]==l) or (b[4]==b[5]==b[6]==l) or (b[7]==b[8]==b[9]==l) #horizontal
		or  (b[1]==b[4]==b[7]==l) or (b[2]==b[5]==b[8]==l) or (b[3]==b[6]==b[9]==l) #vertical
		or  (b[1]==b[5]==b[9]==l) or (b[3]==b[5]==b[7]==l)) #diagonal

#game draw condition
def tie(b):
	for i in range(1, 10):
		if available(b, i):
			return False
	return True

#main
print('Congrats, you get to play Tic Tac Toe with the AI created by Pavan P (yeah, that guy)')
while True:
	mat = [' '] *10
	player, AI = ask()
	turn = coin()
	print(turn,' goes first')
	game = True
	while game:
		if turn=='Player':
			show(mat)
			move = playerMove(mat)
			makeMove(mat,move,player)
			if win(mat,player):
				show(mat)
				print('Congrats, you managed beat my AI by luck')
				game = False
			else:
				if tie(mat):
					show(mat)
					print('Cool, the game is a tie, not bad, I mean given your IQ and all...')
					break
				else:
					turn = 'AI'
		else:
			mov = aiMove(mat,AI)
			makeMove(mat,mov,AI)
			if win(mat,AI):
				show(mat)
				print('As expected, my AI has defeated you, nana nana na.. na.., go and cry now')
				game = False
			else:
				if tie(mat):
					show(mat)
					print('Cool, the game is a tie, not bad, I mean given your IQ and all...')
					break
				else:
					turn = 'Player'
	if not again():
		break		