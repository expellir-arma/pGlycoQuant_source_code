import os


class ProcessSpectra:

    def __init__(self):

        self.CFG_TYPE_MS2 = {'MS2': 0, 'RAW': 1}

    def toolCountCharInString(inputStr, inputChar):

        result = 0

        for c in inputStr:
            if c == inputChar:
                result = result + 1

        return result

    def toolGetWord(inputString, index, d):
        if inputString[0] != d:
            inputString = d + inputString
        if inputString[-1] != d:
            inputString = inputString + d
        p_d = []
        i = 0
        for c in inputString:
            if c == d:
                p_d.append(i)
            i = i + 1
        result = inputString[p_d[index] + 1:p_d[index + 1]]
        return result

    def op_FILL_LIST_PATH_MS(inputPath, inputList, inputExt):

		separator = '|'
		listStrPath = []

		if len(inputPath) < 1:
			print("MSOperator.py, op_FILL_LIST_PATH_MS, MK_1: Path for MS is empty!")

		if inputPath[-1] == separator:
			pass
		else:
			inputPath = inputPath + separator

		nFile = self.toolCountCharInString(inputPath, separator)

		for i in range(nFile):
			listStrPath.append(self.toolGetWord(inputPath, i, separator))

		for strPath in listStrPath:

			if os.path.isdir(strPath):

				for maindir, subdir, file_name_list in os.walk(strPath):

					for filename in file_name_list:

						tmpPath = os.path.join(maindir, filename)  # 合并成一个完整路径

						ext = os.path.splitext(tmpPath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容

						if ext in inputExt:
							inputList.append(tmpPath)

			elif os.path.isfile(strPath):

				inputList.append(strPath)

			else:

				print("MSOperator.py, op_FILL_LIST_PATH_MS, MK_2: Path for MS is illegal!")

    def process(self):

        if self.dp.myCFG.A4_TYPE_MS2 == self.CFG_TYPE_MS2['MS2']:

            op_FILL_LIST_PATH_MS(self.dp.myCFG.A3_PATH_MS2, self.dp.LIST_PATH_MS2, [".ms2", ".MS2"])

        elif self.dp.myCFG.A4_TYPE_MS2 == CFG_TYPE_MS2['RAW']:

            # 转化cfg的raw文件名到ms2文件名，继续读取ms2数据
            LIST_PATH_RAW = []
            op_FILL_LIST_PATH_MS(self.dp.myCFG.A3_PATH_MS2, LIST_PATH_RAW, [".raw"])
            # 先将RAW数据转换成ms1、ms2文件
            functionRaw2MS = CFunctionParseRaw(self.dp)
            functionRaw2MS.raw2MS(LIST_PATH_RAW)
            self.dp.LIST_PATH_MS2 = [i_raw.replace('.raw', '.ms2') for i_raw in LIST_PATH_RAW]

        if self.dp.myCFG.C1_TYPE_QUANT == CFG_TYPE_QUANT['ReportIon']:

            for path in self.dp.LIST_PATH_MS2:
                print(INFO_TO_USER_TaskReadMS2[0] + path)

                functionMS2 = CFuntionParseMS2ForReportIon()
                functionMS2.ms2TOpkl(path)

        elif self.dp.myCFG.C1_TYPE_QUANT == CFG_TYPE_QUANT['LabelA1Ion']:

            for path in self.dp.LIST_PATH_MS2:
                print(INFO_TO_USER_TaskReadMS2[0] + path)

                functionMS2 = CFunctionParseMS2ForLabelA1Ion()
                functionMS2.ms2Topkl(path)

        elif self.dp.myCFG.C1_TYPE_QUANT == 1:

            pass

        else:

            pass


if __name__ == "__main__":
    process = ProcessSpectra()
    process.process()