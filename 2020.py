import os, sys

print ("\033[1;32mSilahkan Masukkan Username Admin& Password Admin")

print ("\033[1;32mAtau silahkan Hubungi King Mr_Z17 untuk mendapatkan User & Pass -nya.....!! ")

username = 'Mr_Z17'      

password = 'YouTube'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("Username Admin : ")

	if uname == username:

		pwd = raw_input("Password admin : ")



		if pwd == password:

			print "\033[1;32mAlhmdllh sudah masuk juga..", 

			sys.exit()



		else:

			print "\033[1;31mMaaf Password Yang Anda Masukkan Salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;31mMaaf Password Yang Anda Masukkan salah...!!\033[00m"

		print "Silahkan segera log-in kembali....!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

