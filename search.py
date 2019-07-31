import os,re


#搜索文件类型
fileType=['.java','.xml','.properties','.yml']
#不需要搜索的文件目录
backDirList=[]
#需要查找的内容
searchContext = ['mobilepos.yeahka.com','inner-lepos.yeahka.com','mobileykpay.yeahka.com','store.yeahka.com','inner-ykpay.yeahka.com']

#搜索结果
searchResult = []

#需要搜索的文件夹
searchFilePath = []

#没有搜索过的文件
exceptionFile = []

def searchText(filePath):
    print('开始搜索文件:' + filePath)
    lineNum = 0
    with open(filePath,'r',encoding='utf-8') as f:
        for line in f.readlines():
            lineNum = lineNum + 1 
            for text in searchContext:
                if line.find(text)>-1:
                # if line.index(text) > -1:
                    print('文件名:' + filePath)
                    print('line:' + str(lineNum))
                    print('内容:' + line)
                    print('---------------------------------------------')
                    searchResult.append({'fileName':filePath,'lineNum':lineNum,'line':line})

def listFile(path):
    files = os.listdir(path)
    for f in files:
        ff = path + '/' + f
        if os.path.isdir(ff):
            if(f[0]=='.'):
                pass
            else:
                listFile(ff)
        else:
            suffix = os.path.splitext(f)[1]
            if suffix in fileType:
                try:
                    searchText(ff)
                except Exception:
                    exceptionFile.append(ff)
                    pass

def writeResultFile(filePath):
    with open(filePath,'w',encoding='utf-8') as f:
        for rs in searchResult:
            f.writelines('文件名:' + str(rs['fileName']).strip() + '\n')
            f.writelines('line:' + str(rs['lineNum']).strip()+ '\n')
            f.writelines('内容:' + str(rs['line']).strip()+ '\n')
            f.writelines('------------------------------------------------------------\n')

if __name__ == '__main__':  
    searchFilePath.append('E:/Work/svn/ysf/trunk')
    searchFilePath.append('E:/Work/svn/posp/ykagent/dev/ykchannel')
    searchFilePath.append('E:/Work/svn/posp/ykagent/dev/ykagent-ui')
    searchFilePath.append('E:/Work/svn/posp/api/dev/api')
    searchFilePath.append('E:/Work/svn/posp/api/dev/cb-service')
    searchFilePath.append('E:/Work/svn/posp/auto_task/trunk/auto_task')
    searchFilePath.append('E:/Work/svn/posp/autoaudit/trunk')
    searchFilePath.append('E:/Work/svn/posp/boss')
    searchFilePath.append('E:/Work/svn/posp/common/trunk/common-utils-2.1')
    searchFilePath.append('E:/Work/svn/posp/customer/dev/customer')
    searchFilePath.append('E:/Work/svn/posp/investment/dev/investment')
    searchFilePath.append('E:/Work/svn/posp/lm_life/trunk/happy-life-merge/happyLife-agent-consumer')
    searchFilePath.append('E:/Work/svn/posp/lm_life/trunk/happy-life-merge/happyLife-customer-consumer')
    searchFilePath.append('E:/Work/svn/posp/lm_life/trunk/happy-life-merge/happy-life-provide')
    searchFilePath.append('E:/Work/svn/posp/mfscript')
    searchFilePath.append('E:/Work/svn/posp/ncpay/dev/nc_payment')
    searchFilePath.append('E:/Work/svn/posp/service/dev/service/custprovide')
    searchFilePath.append('E:/Work/svn/posp/service/dev/service/discovery')
    searchFilePath.append('E:/Work/svn/posp/service/dev/service/provide')
    for path in searchFilePath:
        listFile(path)
    
    writeResultFile('E:/result.log')
    print('打印搜索结果:')
    for sr in searchResult:
        print('文件名:' + str(sr['fileName']).strip() + '\n')
    #print(searchResult) 
    print('异常文件:')
    print(exceptionFile)
