import iexec_doracle as iexec
import random
import time

if __name__ == '__main__':
	try:
		print('Execution start')

		### ORACLE CALL - MODIFY HERE - BEGIN ###
		data  = ( int(time.time()), random.randrange(990, 1011) )
		types = ( 'uint256',        'uint256'                   )
		###  ORACLE CALL - MODIFY HERE - END  ###

	except Exception as e:
		print('Execution failure: {}'.format(e))
		iexec.submitCallback(log=print)
	else:
		print('Execution success')
		iexec.submitCallback(data, types, log=print)
