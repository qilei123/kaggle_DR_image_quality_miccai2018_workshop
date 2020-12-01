import os

def remove_low(record_file_dir,img_dirs):
	count=0
	record_file = open(record_file_dir)
	line = record_file.readline()
	line = record_file.readline()
	if not os.path.exists('low_quality'):
		os.mkdir('low_quality')
	while line:
		line_eles = line.split(',')
		if int(line_eles[1])==0:
			count+=1
			none_exist = True
			if not ('.jpeg' in line_eles[0]):
				line_eles[0]+='.jpeg'			
			for img_dir in img_dirs:
				if os.path.exists('../'+img_dir+'/'+line_eles[0]):			
					#os.system('mv ../'+img_dir+'/'+line_eles[0]+' low_quality')
					none_exist = False
			if none_exist:
				print(line_eles[0])
		line = record_file.readline()
	print(count)

img_dirs = ['dataset_2stages/train_binary/0','dataset_2stages/train_binary/1','dataset_2stages/val_binary/0','dataset_2stages/val_binary/1']
remove_low('quality_csv_label/quality_label_test.csv',img_dirs)
remove_low('quality_csv_label/quality_label_train.csv',img_dirs)
remove_low('quality_csv_label/quality_label_validate.csv',img_dirs)
